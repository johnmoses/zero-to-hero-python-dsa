"""
Minimax helps to get maximum score in a game be checking
all possible moves.
Dept is current dept in game tree

nodeIndex is index of current node in scores[].
if move is of maximizer return true else false
leaves of game tree is stored in scores[]
height is maximum height of Game tree
"""

from __future__ import annotations
import math

def minimax(
    dept: int, node_index: int, is_max: bool,
    scores: list[int], height: float
) -> int:
    if dept < 0:
        raise ValueError("Dept cannot be less than 0")

    if len(scores) == 0:
        raise ValueError("Scores cannot be empty")

    if dept == height:
        return scores[node_index]

    if is_max:
        return max(
            minimax(dept + 1, node_index * 2, False, scores, height),
            minimax(dept + 1, node_index * 2 + 1, False, scores, height),
        )

    return min(
        minimax(dept + 1, node_index * 2, True, scores, height),
        minimax(dept + 1, node_index * 2 + 1, True, scores, height),
    )

def main() -> None:
    scores = [90, 23, 6, 33, 21, 65, 123, 34424]
    height = math.log(len(scores), 2)
    print('Optimal value :', end="")
    print(minimax(0, 0, True, scores, height))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
    