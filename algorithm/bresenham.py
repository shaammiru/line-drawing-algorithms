from typing import Dict


def bres_algorithm(x0: int, y0: int, x1: int, y1: int) -> Dict[str, any]:
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    step_x = 1 if x0 < x1 else -1
    step_y = 1 if y0 < y1 else -1

    if dy > dx:
        result = bres_algorithm(y0, x0, y1, x1)
        return {**result, "is_swapped": True}

    p = 2 * dy - dx
    p0 = p
    x = x0
    y = y0
    ps = []
    coor = []

    while (x != x1) or (y != y1):
        if p <= 0:
            x += step_x
            p += 2 * dy
        else:
            x += step_x
            y += step_y
            p += 2 * (dy - dx)
        ps.append(p)
        coor.append({"x": x, "y": y})

    return {
        "dx": dx,
        "dy": dy,
        "stepX": step_x,
        "stepY": step_y,
        "p0": p0,
        "ps": ps,
        "coor": coor,
        "is_swapped": False,
    }


# result = bres_algorithm(4, 3, 8, -2)
# print(result)
