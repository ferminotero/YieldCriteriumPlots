import matplotlib.pyplot as plt
import numpy as np
import math 
from numpy.linalg import inv
from sympy import *
from os import system
system("clear")

YT = Symbol('YT')
YC = Symbol('YC')

Sx = Symbol('Sx')
Sy = Symbol('Sy')
Sz = Symbol('Sz')
Sxy = Symbol('Sxy')
Sxz = Symbol('Sxz')
Syz = Symbol('Syz')

# ---- Von Mises Behaviour function ----

VM = ((Sx-Sy)**2+(Sy-Sz)**2+(Sz-Sx)**2 + 6*(Sxy**2+Sxz**2+Syz**2))/(2*YT**2)-1

# ---- Drucker Prager Behaviour function ----

A = (2/math.sqrt(3))*(YT*YC)/(YT+YC)
B = (1/math.sqrt(3))*(YT-YC)/(YT+YC)

J2 = ((Sx-Sy)**2+(Sy-Sz)**2+(Sz-Sx)**2 + 6*(Sxy**2+Sxz**2+Syz**2))/6
I1 = (Sx+Sy+Sz)

DP = J2/(A**2) - (B*I1/A)**2 - 2*B*I1/A - 1

# ---- Melro Behaviour function ----

Melro = 6*J2 + 2*I1*(YC-YT)-2*YC*YT

# Plot VM for Sx and Sy

YTv = 10

replacements = [(Sz,0),(Sxy,0),(Sxz,0),(Syz,0),(YT, YTv)]
VMSxSy = simplify(VM.subs(replacements))

replacements = [(Sz,0),(Sy,0),(Sxz,0),(Syz,0),(YT, YTv)]
VMSxSxy = simplify(VM.subs(replacements))

replacements = [(Sx,0),(Sy,0),(Sz,0),(Syz,0),(YT, YTv)]
VMSxySxz = simplify(VM.subs(replacements))


# Plot DP for Sx and Sy

YTv = 10
YCv = 15

replacements = [(Sz,0),(Sxy,0),(Sxz,0),(Syz,0),(YT,YTv),(YC,YCv)]
DPSxSy = simplify(DP.subs(replacements))

replacements = [(Sz,0),(Sy,0),(Sxz,0),(Syz,0),(YT,YTv),(YC,YCv)]
DPSxSxy = simplify(DP.subs(replacements))

replacements = [(Sx,0),(Sy,0),(Sz,0),(Syz,0),(YT,YTv),(YC,YCv)]
DPSxySxz = simplify(DP.subs(replacements))


# Plot Melro for Sx and Sy

YTv = 10
YCv = 15

replacements = [(Sz,0),(Sxy,0),(Sxz,0),(Syz,0),(YT,YTv),(YC,YCv)]
MelroSxSy = simplify(Melro.subs(replacements))

replacements = [(Sz,0),(Sy,0),(Sxz,0),(Syz,0),(YT,YTv),(YC,YCv)]
MelroSxSxy = simplify(Melro.subs(replacements))

replacements = [(Sx,0),(Sy,0),(Sz,0),(Syz,0),(YT,YTv),(YC,YCv)]
MelroSxySxz = simplify(Melro.subs(replacements))

# Ploting

YTplot = YTv + 0.2*YTv
YCplot = -(YCv + 0.5*YCv)
Yshear = YTv*(1/math.sqrt(3)+0.2)

VMSxSyPlot = plot_implicit(Eq(VMSxSy, 0),(Sx, YCplot, YTplot), (Sy, YCplot, YTplot), depth = 1, line_color='blue', show=False)
VMSxSxyPlot = plot_implicit(Eq(VMSxSxy, 0),(Sx, YCplot, YTplot), (Sxy, -Yshear, Yshear), depth = 1, line_color='blue', show=False)
VMSxySxzPlot = plot_implicit(Eq(VMSxySxz, 0),(Sxy, -Yshear, Yshear), (Sxz, -Yshear, Yshear), depth = 1, line_color='blue', show=False)

DPSxSyPlot = plot_implicit(Eq(DPSxSy, 0),(Sx, YCplot, YTplot), (Sy, YCplot, YTplot), depth = 1, line_color='red', show=False)
DPSxSxyPlot = plot_implicit(Eq(DPSxSxy, 0),(Sx, YCplot, YTplot), (Sxy, -Yshear, Yshear), depth = 1, line_color='red', show=False)
DPSxySxzPlot = plot_implicit(Eq(DPSxySxz, 0),(Sxy, -YTplot, YTplot), (Sxz, -Yshear, Yshear), depth = 1, line_color='red', show=False)

MelroSxSyPlot = plot_implicit(Eq(MelroSxSy, 0),(Sx, YCplot, YTplot), (Sy, YCplot, YTplot), depth = 1, line_color='black', show=False)
MelroSxSxyPlot = plot_implicit(Eq(MelroSxSxy, 0),(Sx, YCplot, YTplot), (Sxy, -Yshear, Yshear), depth = 1, line_color='black', show=False)
MelroSxySxzPlot = plot_implicit(Eq(MelroSxySxz, 0),(Sxy, -Yshear, Yshear), (Sxz, -Yshear, Yshear), depth = 1, line_color='black', show=False)


VMSxSyPlot.append(DPSxSyPlot[0])
VMSxSyPlot.append(MelroSxSyPlot[0])
VMSxSyPlot.title = 'VonMises (blue) ; DrukerPrager (red) ; Melro (black)'
VMSxSyPlot.save('/home/fermin/Documents/Python Projects/YiledCriteriumPlots/Sx_Sy.png')

VMSxSxyPlot.append(DPSxSxyPlot[0])
VMSxSxyPlot.append(MelroSxSxyPlot[0])
VMSxSxyPlot.title = 'VonMises (blue) ; DrukerPrager (red) ; Melro (black)'
VMSxSxyPlot.save('/home/fermin/Documents/Python Projects/YiledCriteriumPlots/Sx_Sxy.png')

VMSxySxzPlot.append(DPSxySxzPlot[0])
VMSxySxzPlot.append(MelroSxySxzPlot[0])
VMSxySxzPlot.title = 'VonMises (blue) ; DrukerPrager (red) ; Melro (black)'
VMSxySxzPlot.save('/home/fermin/Documents/Python Projects/YiledCriteriumPlots/Sxy_Sxz.png')

