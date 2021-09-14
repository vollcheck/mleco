from typing import List, Union

from mleco import Numbers


class Matrix:
    # make those lazy using generators?

    def __init__(self, x, *args, **kwargs):
        self.x: List[Numbers] = x

    def __mul__(self, other: Union[int, float, Numbers, "Matrix"]) -> "Matrix":
        if isinstance(other, int) or isinstance(other, float):
            result = [[x * other for x in row] for row in self.x]

        elif isinstance(other, list):
            result = [sum(x * y for x, y in zip(other, row)) for row in self.x]

        elif isinstance(other, Matrix):
            # need to check whether the matrix multiplication is possible
            self_h, self_w = len(self.x), len(self.x[0])
            other_h, other_w = len(other.x), len(other.x[0])
            assert self_w == other_h

            # core algorithm
            result = [
                [sum(a * b for a, b in zip(a_row, b_col)) for b_col in zip(*other.x)]
                for a_row in self.x
            ]

        return result

    def invert(self) -> "Matrix":
        return

    def transpose(self) -> "Matrix":
        t = [[self.x[j][i] for j in range(len(self.x))] for i in range(len(self.x[0]))]
        return t
