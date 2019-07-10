import numpy as np
import matplotlib.pyplot as plt
import json
import glob
import sys
import time
import os
import scipy.constants as cnt
from unwrap.unwrap import unwrap
from mpl_toolkits.axes_grid1 import make_axes_locatable
from linecache import getline, clearcache
from scipy.integrate import simps
from optparse import OptionParser

from OCC.Display.SimpleGui import init_display
from OCC.gp import gp_Pnt, gp_Vec, gp_Dir
from OCC.gp import gp_Ax1, gp_Ax2, gp_Ax3
from OCC.gp import gp_Pln, gp_Trsf, gp_Lin, gp_Elips

if __name__ == "__main__":
    argvs = sys.argv
    parser = OptionParser()
    parser.add_option("--file", dest="file", default="./buckling")
    opt, argc = parser.parse_args(argvs)
    print(argc, opt)

    plf_file = opt.file + ".ply"

    display, start_display, add_menu, add_function_to_menu = init_display()

    display.DisplayShape(gp_Pnt())

    display.FitAll()
    start_display()

