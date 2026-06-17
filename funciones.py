# funciones.py

import numpy as np
import math


def calcular_angulo(x, y):

    g0 = [120, 44]
    g1 = [120, 36]
    p = [x, y]

    v0 = np.array(g0) - np.array(p)
    v1 = np.array(g1) - np.array(p)

    angle = np.arctan2(
        np.linalg.det([v0, v1]),
        np.dot(v0, v1)
    )

    return abs(np.degrees(angle))


def calcular_distancia(x, y):

    x_dist = 120 - x
    y_dist = 0

    if y < 36:
        y_dist = 36 - y

    elif y > 44:
        y_dist = y - 44

    return math.sqrt(
        x_dist**2 + y_dist**2
    )


def dentro_area(x, y):

    if x >= 102 and 18 <= y <= 62:
        return 1

    return 0