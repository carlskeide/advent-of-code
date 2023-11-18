# coding=utf-8
from itertools import cycle
from ..utils import load_input
from ..models import SparseGrid


class ImageGrid(SparseGrid):
    def __init__(self, image, algorithm):
        self.algorithm = algorithm
        self.default = cycle(".#" if algorithm.startswith("#") else "..")

        pixels = {
            (x, y): pixel
            for y, line in enumerate(image.splitlines())
            for x, pixel in enumerate(line)
        }

        super().__init__(pixels)

    def enhance(self):
        x_axis = [x for x, _ in self]
        y_axis = [y for _, y in self]
        search = ((x, y) for y in range(min(y_axis) - 1, max(y_axis) + 2)
                  for x in range(min(x_axis) - 1, max(x_axis) + 2))

        default = next(self.default)
        new_state = {}
        for x, y in search:
            bits = "".join(
                str(int(self.get(pos, default) == "#"))
                for pos in self.area((x - 1, y - 1), (x + 1, y + 1))
            )

            new_state[x, y] = self.algorithm[int(bits, 2)]

        self.state = new_state

    @property
    def pixels(self):
        return sum(pixel == '#' for pixel in self.state.values())

if __name__ == "__main__":
    algorithm, raw_image = load_input(year=2021, day=20, group_lines=True)
    image = ImageGrid(raw_image, algorithm)
    image.enhance()
    image.enhance()
    print(f"Part 1: {image.pixels}")

    for _ in range(48):
        image.enhance()
    print(f"Part 2: {image.pixels}")
