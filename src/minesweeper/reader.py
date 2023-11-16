import sys


class Field(object):
    @classmethod
    def from_string(cls, s):
        field_instance = cls()

        for i, line in enumerate(s.split("\n")):
            line = line.strip()
            if not line:
                continue
            if i == 0:
                continue
            row = [Bomb() if c == "*" else Square() for c in line]
            field_instance.add_row(row)

        field_instance.calculate()
        return field_instance

    def __init__(self):
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)

    def __repr__(self):
        s = ""
        for row in self.rows:
            s += "".join(str(f) for f in row) + "\n"

        return s

    def calculate(self):
        for x, row in enumerate(self.rows):
            for y, f in enumerate(row):
                if isinstance(f, Bomb):
                    continue
                f.value = self.calculate_index(x, y)

    def calculate_index(self, x, y):
        r = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                x_i = x + i
                y_j = y + j
                if x_i < 0 or x_i >= len(self.rows):
                    continue
                if y_j < 0 or y_j >= len(self.rows[0]):
                    continue
                n = self.rows[x_i][y_j]
                if isinstance(n, Bomb):
                    r += 1
        return r

    def __bool__(self):
        return bool(self.rows)


class Bomb:
    def __repr__(self):
        return "*"


class Square:
    def __init__(self):
        self.value = None

    def __repr__(self):
        if self.value is None:
            return "."
        return str(self.value)


def parse_input(stream):
    field = Field()
    counter = 1
    output = f"Field #{counter}:\n"

    for i, line in enumerate(stream):
        line = line.strip()
        if not line:
            continue
        try:
            _, _ = line.split()
        except ValueError:
            pass
        else:
            if not field:
                continue
            output += str(field)
            counter += 1
            output += f"\nField #{counter}:\n"
            field = Field()
            continue
        row = [Bomb() if c == "*" else Square() for c in line]
        field.add_row(row)
        field.calculate()
    output += str(field)

    return output


if __name__ == "__main__":
    print(parse_input(sys.stdin))
    # with open(r"C:\dev\projects\_codingdojo\minesweeper\tests\resources\input_1.txt", "r") as f:
    #     out = parse_input(f)
    # print(out)
