class Maze:

    def __init__(self, N):
        self.N = N
        self.grid = [["█" for _ in range(2 * N + 1)] for _ in range(2 * N + 1)]
        for i in range(1, 2 * N, 2):
            for j in range(1, 2 * N, 2):
                self.grid[i][j] = "·"


    def __str__(self):
        return "\n".join("".join(row) for row in self.grid)

    def __setitem__(self, key, value):
        (x0, y0), (x1, y1) = (key[0], key[1].start), (key[1].stop, key[2])
        if x0 == x1:
            for j in range(min(y0, y1), max(y0, y1) + 2):
                self.grid[j + 2][x0 * 2 + 1] = "·"

        elif y0 == y1:
            for i in range(min(x0, x1), max(x0, x1)):
                self.grid[y0 * 2 + 1][i * 2 + 2] = "·"

    def __getitem__(self, key):
        (x0, y0), (x1, y1) = (key[0], key[1].start), (key[1].stop, key[2])
        visited = set()
        return self.explor(x0 * 2 + 1, y0 * 2 + 1, x1 * 2 + 1, y1 * 2 + 1, visited)

    def explor(self, x, y, target_x, target_y, visited):
        if (x, y) == (target_x, target_y):
            return True
        visited.add((x, y))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.grid[ny][nx] == "·" and (nx, ny) not in visited:
                if self.explor(nx, ny, target_x, target_y, visited):
                    return True
        return False

import sys
exec(sys.stdin.read())