"""
Evaluate a musical composition represented as a `Piece` instance.

Author: Nikolay Lysenko
"""


from collections import Counter
from typing import Any, Callable, Dict, Optional

import numpy as np
from scipy.stats import entropy

from rlmusician.environment.piece import Piece


def evaluate_absence_of_looped_fragments(
        piece: Piece, min_size: int = 8, max_size: Optional[int] = None
) -> float:
    """
    Evaluate non-triviality of a piece based on absence of looped fragments.

    :param piece:
        `Piece` instance
    :param min_size:
        minimum duration of a fragment (in eights)
    :param max_size:
        maximum duration of a fragment (in eights)
    :return:
        multiplied by -1 number of looped fragments
    """
    score = 0
    max_size = max_size or piece.total_duration_in_eights // 2
    for size in range(min_size, max_size + 1):
        for position in range(0, piece.total_duration_in_eights - 2*size + 1):
            fragment = piece.piano_roll[:, position:position+size]
            next_fragment = piece.piano_roll[:, position+size:position+2*size]
            if np.array_equal(fragment, next_fragment):
                score -= 1
    return score


def evaluate_entropy(piece: Piece) -> float:
    """
    Evaluate non-triviality of counterpoint line based on entropy.

    :param piece:
        `Piece` instance
    :return:
        normalized average over all lines entropy of pitches distribution
    """
    positions = [
        x.scale_element.position_in_degrees
        for x in piece.counterpoint
    ]
    counter = Counter(positions)
    lower_position = piece.lowest_element.position_in_degrees
    upper_position = piece.highest_element.position_in_degrees
    elements = piece.scale.elements[lower_position:upper_position + 1]
    distribution = [
        counter[element.position_in_degrees] / len(piece.counterpoint)
        for element in elements
    ]
    raw_score = entropy(distribution)
    max_entropy_distribution = [1 / len(elements) for _ in elements]
    denominator = entropy(max_entropy_distribution)
    score = raw_score / denominator
    return score


def evaluate_climax_explicity(
        piece: Piece,
        shortage_penalty: float = 0.3, duplication_penalty: float = 0.5
) -> float:
    """
    Evaluate goal-orientedness of counterpoint line based on climax explicity.

    :param piece:
        `Piece` instance
    :param shortage_penalty:
        penalty for each scale degree between declared highest pitch of a line
        and actual highest pitch of this line
    :param duplication_penalty:
        penalty for each non-first occurrence of line's highest pitch within
        this line
    :return:
        one minus all applicable penalties
    """
    max_position = piece.counterpoint[0].scale_element.position_in_degrees
    n_duplications = 0
    for line_element in piece.counterpoint[1:]:
        current_position = line_element.scale_element.position_in_degrees
        if current_position == max_position:
            n_duplications += 1
        elif current_position > max_position:
            max_position = current_position
            n_duplications = 0
    declared_max_position = piece.highest_element.position_in_degrees
    shortage = declared_max_position - max_position
    shortage_term = shortage_penalty * shortage
    duplication_term = duplication_penalty * n_duplications
    score = 1 - shortage_term - duplication_term
    return score


def evaluate_number_of_skips(
        piece: Piece, min_n_skips: int = 1, max_n_skips: int = 3
) -> float:
    """
    Evaluate interestingness of counterpoint line based on number of skips.

    :param piece:
        `Piece` instance
    :param min_n_skips:
        minimum number of skips for a line to be interesting
    :param max_n_skips:
        maximum number of skips for a line to be still coherent
    :return:
        indicator whether number of skips lies within a specified range
    """
    n_skips = 0
    for movement in piece.past_movements:
        if abs(movement) > 1:
            n_skips += 1
    score = 1 if min_n_skips <= n_skips <= max_n_skips else 0
    return score


def get_scoring_functions_registry() -> Dict[str, Callable]:
    """
    Get mapping from names of scoring functions to scoring functions.

    :return:
        registry of scoring functions
    """
    registry = {
        'looped_fragments': evaluate_absence_of_looped_fragments,
        'entropy': evaluate_entropy,
        'climax_explicity': evaluate_climax_explicity,
        'number_of_skips': evaluate_number_of_skips,
    }
    return registry


def evaluate(
        piece: Piece,
        scoring_coefs: Dict[str, float],
        scoring_fn_params: Dict[str, Dict[str, Any]],
        verbose: bool = False
) -> float:
    """
    Evaluate piece.

    :param piece:
        `Piece` instance
    :param scoring_coefs:
        mapping from scoring function names to their weights in final score
    :param scoring_fn_params:
        mapping from scoring function names to their parameters
    :param verbose:
        if it is set to `True`, scores are printed with detailing by functions
    :return:
        weighted sum of scores returned by various scoring functions
    """
    score = 0
    registry = get_scoring_functions_registry()
    for fn_name, weight in scoring_coefs.items():
        fn = registry[fn_name]
        fn_params = scoring_fn_params.get(fn_name, {})
        curr_score = weight * fn(piece, **fn_params)
        if verbose:
            print(f'{fn_name:>30}: {curr_score}')  # pragma: no cover
        score += curr_score
    return score
