import math
from typing import Dict


def dda_algorithm(x0: float, y0: float, x1: float, y1: float) -> Dict[str, any]:
    dx = x1 - x0
    dy = y1 - y0
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    x_increment = dx / steps
    y_increment = dy / steps

    x = x0
    y = y0
    coor = []
    rounded_coor = []

    for i in range(steps):
        x += x_increment
        y += y_increment
        coor.append({"x": x, "y": y})

        if x % 0.5 == 0:
            x_round = math.ceil(x)

        if y % 0.5 == 0:
            y_round = math.ceil(y)

        x_round = round(x)
        y_round = round(y)
        rounded_coor.append({"x": x_round, "y": y_round})

    return {
        "dx": dx,
        "dy": dy,
        "steps": steps,
        "x_increment": x_increment,
        "y_increment": y_increment,
        "coor": coor,
        "roundedCoor": rounded_coor,
    }


# result = dda_algorithm(4, 3, 8, -2)
# print(result)
