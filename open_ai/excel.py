from collections import defaultdict

class Excel:

    def __init__(self, height: int, width: str):
        self.grid = defaultdict(int)
        self.height = height
        self.width = width
    
    def column_to_int(self, char):
        return ord(char.lower()) - ord('a')

    def set(self, row: int, column: str, val: int) -> None:
        col = self.column_to_int(column)
        self.grid[(row, col)] = val

    def get(self, row: int, column: str) -> int:
        col = self.column_to_int(column)
        return self.calc_sum(row, col)

    # "A1" -> (1, "A")
    def parse_reference(self, reference):
        col = int(self.column_to_int(reference[0:1]))
        row = int(reference[1:])

        return (row, col)

    # "A1:B2" -> [(1, "A"), (2, "B")]
    def parse_range(self, reference):
        split_val = reference.split(":")
        val1 = split_val[0]

        if len(split_val) == 1:
            return [self.parse_reference(val1)]

        val2 = split_val[1]
        return [self.parse_reference(val1), self.parse_reference(val2)]

    def get_cell_coordinates(self, start_cell, end_cell):
        cells = []

        for r in range(start_cell[0], end_cell[0] + 1):
            for c in range(start_cell[1], end_cell[1] + 1):
                cells.append((r, c))

        return cells

    def calc_sum(self, r, c, memo=None):
        if memo is None:
            memo = {}
        if (r, c) in memo:
            return memo[(r, c)]

        values = self.grid[(r, c)]

        if isinstance(values, int):
            return values

        total = 0
        for ref in values:
            if len(ref) == 1:
                nr, nc = ref[0][0], ref[0][1]
                total += self.calc_sum(nr, nc, memo)
            else:
                cells = self.get_cell_coordinates(ref[0], ref[1])

                for nr, nc in cells:
                    total += self.calc_sum(nr, nc, memo)

        memo[(r, c)] = total
        return total

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        col = self.column_to_int(column)

        references = []
        for number in numbers:
            references.append(self.parse_range(number))
        
        self.grid[(row, col)] = references

        total = self.calc_sum(row, col)

        return total
