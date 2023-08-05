"""
@title  : create directional vectors without undesirable outputs (g_x, g_y)
@Author : Sheng Dai, Timo Kuosmanen
@Mail   : sheng.dai@aalto.fi (S. Dai); timo.kuosmanen@aalto.fi (T. Kuosmanen)
@Date   : 2020-04-27
"""

import numpy as np


def dvb(gx, gy, n, m, p):
    # directional vectors

    # g_x
    if m == 1:
        gx = np.repeat(gx, n)
        gx = gx.tolist()

    if m == 2:
        gx1 = np.repeat(gx[0], n)
        gx1 = np.asmatrix(gx1).T
        gx2 = np.repeat(gx[1], n)
        gx2 = np.asmatrix(gx2).T
        gx = np.concatenate((gx1, gx2), axis=1)
        gx = gx.tolist()

    if m == 3:
        gx1 = np.repeat(gx[0], n)
        gx1 = np.asmatrix(gx1).T
        gx2 = np.repeat(gx[1], n)
        gx2 = np.asmatrix(gx2).T
        gx3 = np.repeat(gx[2], n)
        gx3 = np.asmatrix(gx3).T
        gx = np.concatenate((gx1, gx2, gx3), axis=1)
        gx = gx.tolist()

    # g_y
    if p == 1:
        gy = np.repeat(gy, n)
        gy = gy.tolist()

    if p == 2:
        gy1 = np.repeat(gy[0], n)
        gy1 = np.asmatrix(gy1).T
        gy2 = np.repeat(gy[1], n)
        gy2 = np.asmatrix(gy2).T
        gy = np.concatenate((gy1, gy2), axis=1)
        gy = gy.tolist()

    if p == 3:
        gy1 = np.repeat(gy[0], n)
        gy1 = np.asmatrix(gy1).T
        gy2 = np.repeat(gy[1], n)
        gy2 = np.asmatrix(gy2).T
        gy3 = np.repeat(gy[2], n)
        gy3 = np.asmatrix(gy3).T
        gy = np.concatenate((gy1, gy2, gy3), axis=1)
        gy = gy.tolist()

    return gx, gy
