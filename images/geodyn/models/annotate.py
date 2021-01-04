from pathlib import Path
from typing import NamedTuple
from copy import copy 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as patches

from scipy.special import binom

bernstein = lambda n, k, t: binom(n,k)* t**k * (1.-t)**(n-k)


def bezier(points, num=200):
    N = len(points)
    t = np.linspace(0, 1, num=num)
    curve = np.zeros((num, 2))
    for i in range(N):
        curve += np.outer(bernstein(N - 1, i, t), points[i])
    return curve

class Rectangle(NamedTuple):
    bottom: int
    left: int
    width: int
    height: int


def add_image(ax, path: str):
    ax.set_frame_on(False)
    ax.set_xticks([])
    ax.set_yticks([])

    img = plt.imread(path)
    ax.imshow(img)


basin_rect = Rectangle(
    left=1425,
    bottom=350,
    width=700,
    height=300,
)

def make_rect(ax):
    b = basin_rect

    return patches.Rectangle((b.left, b.bottom), b.width, b.height,
                             linewidth=2.0, edgecolor="black",
                             facecolor='none')


nodes = np.array([
    (2600, 1000),
    (2400, 975),
    (2250, 950),
    (2200, 940),
    (2150, 940),
    (2100, 940),
    (2050, 940),
    (1975, 945),
    (1965, 950),
    (1950, 1010),
    (2000, 1070),
    (2050, 1170),
    (2070, 1220),
    (2100, 1320),
    (2150, 1420),
    (2170, 1520),
    (2200, 1620),
    (2250, 1820),
    (2300, 1850),
    (2300, 1900),
])

vel_nodes = [
    nodes,
    nodes[1:-2, :] * 1.05,
    nodes[2:-2, :] * 1.085,
]

def main():
    images = Path("/home/istvan/packages/src/github.com/bozso/texfiles/images/")
    geodyn = images / "geodyn"
    models = geodyn / "models"

    b_rect= make_rect(basin_rect)
    vel_curves = [bezier(node, num=128) for node in vel_nodes]
    img_paths = [
        "visc_vel_basin.png",
        "stress_xx.png",
    ]

    for img_path in img_paths:
        f, ax = plt.subplots()
        add_image(ax=ax, path=str(models / img_path))
        ax.add_patch(copy(b_rect))

        for curve in vel_curves:
            curve = copy(curve)
            ax.plot(curve[:, 0], curve[:, 1], color="black")

        f.savefig(models.joinpath("%s_annot.png" % img_path.split(".")[0]),
                  dpi=350, bbox_inches='tight')
    

if __name__ == "__main__":
    main()
