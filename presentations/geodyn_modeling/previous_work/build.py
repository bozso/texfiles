from sys import path

path.append("/home/istvan/progs/utils")

from utils import HTML

src = ["prev.cml"]

h = HTML()

h.sources(src)
