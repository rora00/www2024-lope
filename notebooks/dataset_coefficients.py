import numpy as np


x_s_coef1 = np.array([
    [-0.2,  1.1, -0.9],
]).T * (1 / 3)


x_s_coef2 = np.array([
    [-0.2,  1.0, -0.8],
    [0.0, 0.1, -0.1],
]).T * (2 / 3)


x_s_coef3 = np.array([
    [0.1, 0.5, -0.35],
    [0.0, 0.05, -0.05],
    [-0.3, 0.55, -0.5],
]).T


x_s_coef4 = np.array([
    [0.1, 0.4, -0.35],
    [0.0, 0.05, -0.05],
    [-0.25, 0.4, -0.5],
    [-0.05, 0.25, 0.0],
]).T * (4 / 3)


x_s_coef5 = np.array([
    [0.1, 0.4, -0.35],
    [0.0, 0.05, -0.05],
    [-0.25, 0.4, -0.5],
    [-0.05, 0.25, 0.0],
    [0.0, 0.0, 0.0],
]).T * (5 / 3)


coef_dict = {
    1: x_s_coef1,
    2: x_s_coef2,
    3: x_s_coef3,
    4: x_s_coef4,
    5: x_s_coef5,
}