from sys import path

path.append("/home/istvan/progs/utils")

from utils import HTML

src = ["full.cml"]

h = HTML()

h.sources(src)
