# coding=utf-8
from ..utils import load_input


class Navigator:
    def __init__(self, face):
        self.face = face
        self.position = {"x": 0, "y": 0}

    def follow(self, instructions):
        plan = ((line[:1], int(line[1:])) for line in instructions)

        for action, arg in plan:
            if action == "F":
                self.forward(arg)

            elif action in "NSEW":
                self.move(action, arg)

            elif action in "LR":
                self.turn(action, arg)

            else:
                raise NotImplementedError(action)

    def forward(self, units):
        self.move(self.face, units)

    def move(self, direction, units):
        if direction == "N":
            self.position["y"] += units
        elif direction == "S":
            self.position["y"] -= units
        elif direction == "E":
            self.position["x"] += units
        elif direction == "W":
            self.position["x"] -= units

    def turn(self, direction, degrees):
        card = list("NESW" * 2)
        if direction == "L":
            card.reverse()

        steps = degrees // 90
        self.face = card[card.index(self.face) + steps]

    @property
    def distance(self):
        return sum(map(abs, self.position.values()))


class WaypointNavigator(Navigator):
    def __init__(self, face):
        super().__init__(face)
        self.target = {"x": 10, "y": 1}

    def forward(self, units):
        self.position["x"] += self.target["x"] * units
        self.position["y"] += self.target["y"] * units

    def move(self, direction, units):
        if direction == "N":
            self.target["y"] += units
        elif direction == "S":
            self.target["y"] -= units
        elif direction == "E":
            self.target["x"] += units
        elif direction == "W":
            self.target["x"] -= units

    def turn(self, direction, degrees):
        for step in range((degrees // 90)):
            self.target["x"], self.target["y"] = self.target["y"], self.target["x"]
            self.target["x" if direction == "L" else "y"] *= -1


if __name__ == "__main__":
    task_input = load_input(year=2020, day=12)

    ship = Navigator(face="E")
    ship.follow(task_input)
    print(f"Part 1: {ship.distance}")

    waypoint_ship = WaypointNavigator(face="E")
    waypoint_ship.follow(task_input)
    print(f"Part 2: {waypoint_ship.distance}")
