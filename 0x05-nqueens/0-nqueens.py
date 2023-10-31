#!/usr/bin/python3

""" The N queens puzzle is the challenge of placing N non-attacking
 queens on an N×N chessboard
"""
import sys


def solve_nqueens(n):
    """
    Solve the N queens problem using backtracking.

    Args:
        n (int): The number of queens and the size of the chess board (n x n).

    Returns:
        list: A list of all possible solutions. Each solution is represented
          as a list of integers,
              where the value of i-th integer represents the column number of
                the queen placed in the i-th row.
    """

    def can_place(pos, ocuppied_positions):
        """
        Check if a queen can be placed at the given position.

        Args:
            pos (int): The position to check.
            ocuppied_positions (list): A list of positions already occupied
              by other queens.

        Returns:
            bool: True if a queen can be placed at pos, False otherwise.
        """
        for i in range(len(ocuppied_positions)):
            if (
                ocuppied_positions[i] == pos
                or ocuppied_positions[i] - i == pos - len(ocuppied_positions)
                or ocuppied_positions[i] + i == pos + len(ocuppied_positions)
            ):
                return False
        return True

    def place_queens(n, index, ocuppied_positions, all_ocuppied_positions):
        """
        Place queens on the board using backtracking.

        Args:
            n (int): The number of queens and the size of the chess board
              (n x n).
            index (int): The current index (row number) to place a queen.
            ocuppied_positions (list): A list of positions already occupied
              by other queens.
            all_ocuppied_positions (list): A list to store all possible
              solutions.
        """
        if index == n:
            all_ocuppied_positions.append(ocuppied_positions[:])
            return

        for i in range(n):
            if can_place(i, ocuppied_positions):
                ocuppied_positions.append(i)
                place_queens(n, index + 1, ocuppied_positions,
                             all_ocuppied_positions)
                ocuppied_positions.pop()

    all_ocuppied_positions = []
    place_queens(n, 0, [], all_ocuppied_positions)
    return all_ocuppied_positions


def main():
    """
    The main function that checks the input and calls solve_nqueens
      to find solutions.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        result = [[i, solution[i]] for i in range(n)]
        print(result)


if __name__ == "__main__":
    main()
