from enum import Enum


class Direction(Enum):
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4


class Solution:
    def generate_matrix(self, n: int) -> list[list[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        row, col = 0, 0
        curr = 1
        direction = Direction.RIGHT
        filled = 0

        while matrix[row][col] == 0:
            matrix[row][col] = curr
            curr += 1
            filled += 1
            if filled == n * n:
                break
            row, col, direction = self.advance_in_direction(matrix, direction, n, row, col)
        return matrix

    def advance_in_direction(self, matrix, direction: Direction, n: int, row: int, col: int) -> (int, int, Direction):
        if direction == Direction.RIGHT:
            row, col, direction_changed = self.advance_right(matrix, n, row, col)
            if direction_changed:
                direction = Direction.DOWN
                row, col, _ = self.advance_down(matrix, n, row, col)
            return row, col, direction

        if direction == Direction.DOWN:
            row, col, direction_changed =  self.advance_down(matrix, n, row, col)
            if direction_changed:
                direction = Direction.LEFT
                row, col, _ = self.advance_left(matrix, row, col)
            return row, col, direction

        if direction == Direction.LEFT:
            row, col, direction_changed =  self.advance_left(matrix, row, col)
            if direction_changed:
                direction = Direction.UP
                row, col, _ = self.advance_up(matrix, row, col)
            return row, col, direction

        if direction == Direction.UP:
            row, col, direction_changed =  self.advance_up(matrix, row, col)
            if direction_changed:
                direction = Direction.RIGHT
                row, col, _ = self.advance_right(matrix, n, row, col)

        return row, col, direction

    def advance_right(
        self,
        matrix: list[list[int]],
        n: int,
        row: int,
        col: int
    ) -> (int, int, Direction):
        col += 1
        direction_changed = False
        if col == n or matrix[row][col] != 0:
            col -= 1
            direction_changed = True
        return row, col, direction_changed

    def advance_down(
        self,
        matrix: list[list[int]],
        n: int,
        row: int,
        col: int
    ) -> (int, int, Direction):
        row += 1
        direction_changed = False
        if row == n or matrix[row][col] != 0:
            row -= 1
            direction_changed = True
        return row, col, direction_changed

    def advance_left(
        self,
        matrix: list[list[int]],
        row: int,
        col: int
    ) -> (int, int, Direction):
        col -= 1
        direction_changed = False
        if col == -1 or matrix[row][col] != 0:
            col += 1
            direction_changed = True
        return row, col, direction_changed

    def advance_up(
        self,
        matrix: list[list[int]],
        row: int,
        col: int
    ) -> (int, int, bool):
        row -= 1
        direction_changed = False
        if row == -1 or matrix[row][col] != 0:
            row += 1
            direction_changed = True
        return row, col, direction_changed