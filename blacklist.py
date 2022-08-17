class Board:
    def __init__(self, size=6):
        self.size = size
        self.field = [["O"] * size for _ in range(size)]

    def __str__(self):
        numbs = "  | 1 | 2 | 3 | 4 | 5 | 6 |"

        for i, row in enumerate(self.field):
            numbs += f"\n{i + 1} | " + " | ".join(row) + " |"
        return numbs


d = Board()
print(d)

class CreateShips:

