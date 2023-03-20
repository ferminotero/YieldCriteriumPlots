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

#S = Symbol [6]
# Definer a Stress como un array simbolic

Ax = Symbol('Ax')
Ay = Symbol('Ay')
Az = Symbol('Az')
Axy = Symbol('Axy')
Axz = Symbol('Axz')
Ayz = Symbol('Ayz')

# Definar A como un array simbolic

# Definir un RS real stress arry simbolic, donde cada componente sea Sx*Ax 

#RS = matmul(A,S)

# ---- Von Mises Behaviour function ----

VM = ((Sx*Ax-Sy*Ay)**2+(Sy*Ay-Sz*Az)**2+(Sz*Az-Sx*Ax)**2 + 6*((Sxy*Axy)**2+(Sxz*Axz)**2+(Syz*Ayz)**2))/(2*YT**2)-1

# ---- Drucker Prager Behaviour function ----

# A = (2/math.sqrt(3))*(YT*YC)/(YT+YC)
# B = (1/math.sqrt(3))*(YT-YC)/(YT+YC)

# J2 = ((Sx-Sy)**2+(Sy-Sz)**2+(Sz-Sx)**2 + 6*(Sxy**2+Sxz**2+Syz**2))/6
# I1 = (Sx+Sy+Sz)

# DP = J2/(A**2)-(B*I1/A)**2-2*B*I1/A - 1

# # ---- Melro Behaviour function ----

# Melro = 6*J2 + 2*I1*(YC-YT)-2*YC*YT

# # ---- Melro Potential function ----

# vp = Symbol('vp')

# alpha = (9/2)*(1-2*vp)/(1+vp)

# MelroPtt = 3*J2 + (alpha/9)*I1**2

# Plotting

YTv = 10
YCv = 15

replacementsA = [(Ax,2),(Ay,1),(Az,1),(Axy,1),(Axz,1),(Ayz,1)]

# Plot VM 

YTv = 10

replacements = [(Sz,0),(Sxy,0),(Sxz,0),(Syz,0),(YT, YTv),(Ax,2),(Ay,1),(Az,1),(Axy,1),(Axz,1),(Ayz,1)]
VMSxSy = simplify(VM.subs(replacements))

replacements = [(Sz,0),(Sy,0),(Sxz,0),(Syz,0),(YT, YTv), (Ax,2),(Ay,1),(Az,1),(Axy,1),(Axz,1),(Ayz,1)]
VMSxSxy = simplify(VM.subs(replacements))

replacements = [(Sx,0),(Sy,0),(Sz,0),(Syz,0),(YT, YTv),(Ax,2),(Ay,1),(Az,1),(Axy,1),(Axz,1),(Ayz,1)]
VMSxySxz = simplify(VM.subs(replacements))


# # Plot DP 

# YTv = 10
# YCv = 15

# replacements = [(Sz,0),(Sxy,0),(Sxz,0),(Syz,0),(YT,YTv),(YC,YCv)]
# DPSxSy = simplify(DP.subs(replacements))

# replacements = [(Sz,0),(Sy,0),(Sxz,0),(Syz,0),(YT,YTv),(YC,YCv)]
# DPSxSxy = simplify(DP.subs(replacements))

# replacements = [(Sx,0),(Sy,0),(Sz,0),(Syz,0),(YT,YTv),(YC,YCv)]
# DPSxySxz = simplify(DP.subs(replacements))


# # Plot Melro 

# YTv = 10
# YCv = 15

# replacements = [(Sz,0),(Sxy,0),(Sxz,0),(Syz,0),(YT,YTv),(YC,YCv)]
# MelroSxSy = simplify(Melro.subs(replacements))

# replacements = [(Sz,0),(Sy,0),(Sxz,0),(Syz,0),(YT,YTv),(YC,YCv)]
# MelroSxSxy = simplify(Melro.subs(replacements))

# replacements = [(Sx,0),(Sy,0),(Sz,0),(Syz,0),(YT,YTv),(YC,YCv)]
# MelroSxySxz = simplify(Melro.subs(replacements))


# # Plot Melro Potential

# vp1 = 0.2

# replacements = [(Sz,0),(Sxy,0),(Sxz,0),(Syz,0),(vp,vp1)]
# MelroPtt02SxSy = simplify(MelroPtt.subs(replacements))

# replacements = [(Sz,0),(Sy,0),(Sxz,0),(Syz,0),(vp,vp1)]
# MelroPtt02SxSxy = simplify(MelroPtt.subs(replacements))

# replacements = [(Sx,0),(Sy,0),(Sz,0),(Syz,0),(vp,vp1)]
# MelroPtt02SxySxz = simplify(MelroPtt.subs(replacements))

# vp2 = 0.35

# replacements = [(Sz,0),(Sxy,0),(Sxz,0),(Syz,0),(vp,vp2)]
# MelroPtt35SxSy = simplify(MelroPtt.subs(replacements))

# replacements = [(Sz,0),(Sy,0),(Sxz,0),(Syz,0),(vp,vp2)]
# MelroPtt35SxSxy = simplify(MelroPtt.subs(replacements))

# replacements = [(Sx,0),(Sy,0),(Sz,0),(Syz,0),(vp,vp2)]
# MelroPtt35SxySxz = simplify(MelroPtt.subs(replacements))


# vp3 = 0.5

# replacements = [(Sz,0),(Sxy,0),(Sxz,0),(Syz,0),(vp,vp3)]
# MelroPtt05SxSy = simplify(MelroPtt.subs(replacements))

# replacements = [(Sz,0),(Sy,0),(Sxz,0),(Syz,0),(vp,vp3)]
# MelroPtt05SxSxy = simplify(MelroPtt.subs(replacements))

# replacements = [(Sx,0),(Sy,0),(Sz,0),(Syz,0),(vp,vp3)]
# MelroPtt05SxySxz = simplify(MelroPtt.subs(replacements))


# Ploting

YTplot = YTv + 0.2*YTv
YCplot = -(YCv + 0.5*YCv)
Yshear = YTv*(1/math.sqrt(3)+0.2)

VMSxSyPlot = plot_implicit(Eq(VMSxSy, 0),(Sx, YCplot, YTplot), (Sy, YCplot, YTplot), depth = 1, line_color='blue', show=False)
VMSxSxyPlot = plot_implicit(Eq(VMSxSxy, 0),(Sx, YCplot, YTplot), (Sxy, -Yshear, Yshear), depth = 1, line_color='blue', show=False)
VMSxySxzPlot = plot_implicit(Eq(VMSxySxz, 0),(Sxy, -Yshear, Yshear), (Sxz, -Yshear, Yshear), depth = 1, line_color='blue', show=False)

# DPSxSyPlot = plot_implicit(Eq(DPSxSy, 0),(Sx, YCplot, YTplot), (Sy, YCplot, YTplot), depth = 1, line_color='red', show=False)
# DPSxSxyPlot = plot_implicit(Eq(DPSxSxy, 0),(Sx, YCplot, YTplot), (Sxy, -Yshear, Yshear), depth = 1, line_color='red', show=False)
# DPSxySxzPlot = plot_implicit(Eq(DPSxySxz, 0),(Sxy, -YTplot, YTplot), (Sxz, -Yshear, Yshear), depth = 1, line_color='red', show=False)

# MelroSxSyPlot = plot_implicit(Eq(MelroSxSy, 0),(Sx, YCplot, YTplot), (Sy, YCplot, YTplot), depth = 1, line_color='black', show=False)
# MelroSxSxyPlot = plot_implicit(Eq(MelroSxSxy, 0),(Sx, YCplot, YTplot), (Sxy, -Yshear, Yshear), depth = 1, line_color='black', show=False)
# MelroSxySxzPlot = plot_implicit(Eq(MelroSxySxz, 0),(Sxy, -Yshear, Yshear), (Sxz, -Yshear, Yshear), depth = 1, line_color='black', show=False)

# MelroPtt02SxSyPlot = plot_implicit(Eq(MelroPtt02SxSy, 100),(Sx, -YTplot, YTplot), (Sy, -YTplot, YTplot), line_color='red', show=False)
# MelroPtt02SxSxyPlot = plot_implicit(Eq(MelroPtt02SxSxy, 100),(Sx, -YTplot, YTplot), (Sxy, -Yshear, Yshear), line_color='red', show=False)
# MelroPtt02SxySxzPlot = plot_implicit(Eq(MelroPtt02SxySxz, 100),(Sxy, -Yshear, Yshear), (Sxz, -Yshear, Yshear), line_color='red', show=False)

# MelroPtt35SxSyPlot = plot_implicit(Eq(MelroPtt35SxSy, 100),(Sx, -YTplot, YTplot), (Sy, -YTplot, YTplot), line_color='black', show=False)
# MelroPtt35SxSxyPlot = plot_implicit(Eq(MelroPtt35SxSxy, 100),(Sx, -YTplot, YTplot), (Sxy, -Yshear, Yshear),line_color='black', show=False)
# MelroPtt35SxySxzPlot = plot_implicit(Eq(MelroPtt35SxySxz, 100), (Sxy, -Yshear, Yshear), (Sxz, -Yshear, Yshear), line_color='black', show=False)

# MelroPtt05SxSyPlot = plot_implicit(Eq(MelroPtt05SxSy, 100),(Sx, -YTplot, YTplot), (Sy, -YTplot, YTplot), line_color='blue', show=False)
# MelroPtt05SxSxyPlot = plot_implicit(Eq(MelroPtt05SxSxy, 100),(Sx, -YTplot, YTplot), (Sxy, -Yshear, Yshear), line_color='blue', show=False)
# MelroPtt05SxySxzPlot = plot_implicit(Eq(MelroPtt05SxySxz, 100), (Sxy, -Yshear, Yshear), (Sxz, -Yshear, Yshear), line_color='blue', show=False)


#VMSxSyPlot.append(DPSxSyPlot[0])
#VMSxSyPlot.append(MelroSxSyPlot[0])
VMSxSyPlot.title = 'VonMises (blue) ; DrukerPrager (red) ; Melro (black)'
VMSxSyPlot.save('/home/fotero/Documents/YiledCriteriumPlots/Sx_Sy.png')

# VMSxSxyPlot.append(DPSxSxyPlot[0])
# VMSxSxyPlot.append(MelroSxSxyPlot[0])
VMSxSxyPlot.title = 'VonMises (blue) ; DrukerPrager (red) ; Melro (black)'
VMSxSxyPlot.save('/home/fotero/Documents/YiledCriteriumPlots/Sx_Sxy.png')

# VMSxySxzPlot.append(DPSxySxzPlot[0])
# VMSxySxzPlot.append(MelroSxySxzPlot[0])
VMSxySxzPlot.title = 'VonMises (blue) ; DrukerPrager (red) ; Melro (black)'
VMSxySxzPlot.save('/home/fotero/Documents/YiledCriteriumPlots/Sxy_Sxz.png')


# MelroPtt02SxSyPlot.append(MelroPtt35SxSyPlot[0])
# MelroPtt02SxSyPlot.append(MelroPtt05SxSyPlot[0])
# MelroPtt02SxSyPlot.append(VMSxSyPlot[0])
# MelroPtt02SxSyPlot.title = 'vp = 0.2 (red) ; vp = 0.35 (black) ; vp = 0.5 (blue)'
# MelroPtt02SxSyPlot.save('/home/fotero/Documents/YiledCriteriumPlots/Sx_Sy2.png')
# MelroPtt02SxSxyPlot.append(MelroPtt35SxSxyPlot[0])
# MelroPtt02SxSxyPlot.append(MelroPtt05SxSxyPlot[0])
# MelroPtt02SxSxyPlot.append(VMSxSxyPlot[0])
# MelroPtt02SxSxyPlot.title = 'vp = 0.2 (red) ; vp = 0.35 (black) ; vp = 0.5 (blue)'
# MelroPtt02SxSxyPlot.save('/home/fotero/Documents/YiledCriteriumPlots/Sx_Sxy2.png')
# MelroPtt02SxySxzPlot.append(MelroPtt35SxySxzPlot[0])
# MelroPtt02SxySxzPlot.append(MelroPtt05SxySxzPlot[0])
# MelroPtt02SxySxzPlot.append(VMSxySxzPlot[0])
# MelroPtt02SxySxzPlot.title = 'vp = 0.2 (red) ; vp = 0.35 (black) ; vp = 0.5 (blue)'
# MelroPtt02SxySxzPlot.save('/home/fotero/Documents/YiledCriteriumPlots/Sxy_Sxz2.png')
