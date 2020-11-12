import functools as ft
import matplotlib.pyplot as plt
import math
import numpy as np

from pathlib import Path

tft = 12
ft = 14
pi = np.pi
pi_4 = pi * 4.0
pi_2 = pi * 2.0

def wrap(phases):
    return (phases + pi) % pi_2 - pi

class Wavelength(float):
    def deformation(self, val):
        return (pi_4 * val) / self
    
    def height_ambiguity(self, dist, inc_angle, b_perp):
        wl = self * 1.0e-2
        return (wl * dist * np.sin(np.radians(inc_angle))) / (2 * b_perp)
    

class band(object):
    c = Wavelength(5.6)
    
def main():
    img = Path("..").joinpath("..", "images")
    theory = img.joinpath("insar", "theory")
    
    d = np.arange(0.0, 10.0, 0.01)
    
    f = plt.figure()
    ax = f.add_axes((0.2, 0.1, 0.8, 0.8))
    
    ax.plot(d, wrap(band.c.deformation(d)) / pi)
    ax.grid()
    ax.tick_params(labelsize=tft)
    ax.set_xlabel("Deformation [cm]", fontsize=ft)
    ax.set_ylabel(r"Interferometry phase [$\pi$]", fontsize=ft)
    f.savefig(theory / "deform.png", dpi=140)
    
    b = np.arange(10.0, 100.0, 1.0)
    
    f = plt.figure()
    ax = f.add_axes((0.2, 0.1, 0.8, 0.8))
    
    ax.plot(
        b,
        band.c.height_ambiguity(
            dist=800.0e3, inc_angle=23.0, b_perp=b
        )
    )
    ax.grid()
    ax.tick_params(labelsize=tft)
    ax.set_xlabel("Baseline [m]", fontsize=ft)
    ax.set_ylabel("Height Ambiguity [m]", fontsize=ft)
    f.savefig(theory / "baseline_vs_topo_ambig.png", dpi=140)
    
    
if __name__ == "__main__":
    main()
