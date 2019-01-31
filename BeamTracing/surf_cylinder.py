from OCC.Display.SimpleGui import init_display
from OCC.gp import gp_Pnt, gp_Vec, gp_Dir
from OCC.gp import gp_Ax1, gp_Ax2, gp_Ax3
from OCC.gp import gp_Circ, gp_Circ2d
from OCC.Geom import Geom_Plane, Geom_Surface, Geom_BSplineSurface
from OCC.Geom import Geom_Curve, Geom_Line, Geom_Ellipse
from OCC.Geom import Geom_Circle
from OCC.BRep import BRep_Tool
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeFace
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeWire
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeShell
from OCC.BRepOffsetAPI import BRepOffsetAPI_ThruSections
from OCC.BRepOffsetAPI import BRepOffsetAPI_MakePipe
from OCC.BRepPrimAPI import BRepPrimAPI_MakePrism
from OCCUtils.Construct import vec_to_dir, dir_to_vec
from OCCUtils.Construct import make_edge
import numpy as np
import matplotlib.pyplot as plt
import json
import glob
import sys
import time
import os
from unwrap.unwrap import unwrap
from mpl_toolkits.axes_grid1 import make_axes_locatable
from linecache import getline, clearcache
from scipy.integrate import simps
from optparse import OptionParser
sys.path.append(os.path.join('../'))


if __name__ == "__main__":
    from src.fileout import occ_to_grasp_cor, occ_to_grasp_rim
    from src.geomtory import curvature, grasp_sfc
    from src.geomtory import fit_surf
    from src.pyocc.surface import surf_spl
    from src.pyocc.export import export_STEPFile_single

    argvs = sys.argv
    parser = OptionParser()
    parser.add_option("--dir", dest="dir", default="./")
    parser.add_option("--surf", dest="surf", default="cylinder")
    opt, argc = parser.parse_args(argvs)
    print(argc, opt)

    display, start_display, add_menu, add_function_to_menu = init_display()

    api = BRepOffsetAPI_ThruSections()

    pt = np.linspace(0, 100, 10)
    for d in pt:
        pnt = gp_Pnt(0, 0, d)
        d_z = gp_Dir(0, 0, 1)
        obj = Geom_Circle(gp_Ax2(pnt, d_z), 10).Circ()
        wxy = BRepBuilderAPI_MakeWire(
            BRepBuilderAPI_MakeEdge(obj).Edge()).Wire()
        display.DisplayShape(wxy)
        api.AddWire(wxy)

    api.Build()
    surf = api.Shape()
    display.DisplayShape(surf)

    export_STEPFile_single(surf, opt.dir + opt.surf + ".stp")

    display.FitAll()
    start_display()
