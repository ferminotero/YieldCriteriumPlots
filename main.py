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

DP = ((Sx-Sy)**2+(Sy-Sz)**2+(Sz-Sx)**2 + 6*(Sxy**2+Sxz**2+Syz**2))/(6*A**2) - (B*(Sx+Sy+Sz)/A)**2-2*B*(Sx+Sy+Sz)/A-1

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

# Ploting

YTplot = YTv + 0.2*YTv
YCplot = -(YCv + 0.5*YCv)

VMSxSyPlot = plot_implicit(Eq(VMSxSy, 0),(Sx, YCplot, YTplot), (Sy, YCplot, YTplot), label='VM', line_color='blue', show=False, legend=True)
VMSxSxyPlot = plot_implicit(Eq(VMSxSxy, 0),(Sx, YCplot, YTplot), (Sxy, YCplot, YTplot),line_color='blue', show=False, legend=True)
VMSxySxzPlot = plot_implicit(Eq(VMSxySxz, 0),(Sxy, YCplot, YTplot), (Sxz, YCplot, YTplot),line_color='blue', show=False, legend=True)

DPSxSyPlot = plot_implicit(Eq(DPSxSy, 0),(Sx, YCplot, YTplot), (Sy, YCplot, YTplot), label='DP', line_color='red', show=False, legend=True)
DPSxSxyPlot = plot_implicit(Eq(DPSxSxy, 0),(Sx, YCplot, YTplot), (Sxy, YCplot, YTplot), line_color='red', show=False, legend=True)
DPSxySxzPlot = plot_implicit(Eq(DPSxySxz, 0),(Sxy, YCplot, YTplot), (Sxz, YCplot, YTplot), line_color='red', show=False, legend=True)



VMSxSyPlot.append(DPSxSyPlot[0])
VMSxSyPlot.show()
VMSxSxyPlot.append(DPSxSxyPlot[0])
VMSxSxyPlot.show()
VMSxySxzPlot.append(DPSxySxzPlot[0])
VMSxySxzPlot.show()

#fig, (VMSxSyPlot, DPSxSyPlot) = plt.subplots(1, 2, figsize=(8, 4.5))
#fig, ax1 = plt.subplots()
#ax1.title.set_text('Von Mises')
#ax1.set_ylabel("Sy")
#ax1.set_xlabel("Sx")
#TBTTauCorrected = [num*factorK for num in TBTTau]
#ax1.plot(SxPos, SyPosPos, label = "line 1", linestyle=":", color="tab:orange")
#ax1.plot(SxPos, SyPosNeg, label = "line 1", linestyle=":", color="tab:orange")
#ax1.plot(SxNeg, SyNegPos, label = "line 1", linestyle=":", color="tab:orange")
#ax1.plot(SxNeg, SyNegNeg, label = "line 1", linestyle=":", color="tab:orange")
#ax1.plot(TBTTauCorrected, Zpos, label = "line 1",                color="tab:orange")
#ax1.plot(PSTau, Zpos, label = "line 1",                color="tab:blue")
#ax2.plot(integrantTB,          Zpos, label = "TB Original",  linestyle=":", color="tab:orange")
#ax2.plot(integrantTBcorrected, Zpos, label = "TB Corrected",                color="tab:orange")
#ax2.plot(integrantPS,          Zpos, label = "PS",                          color="tab:blue")
#ax1.set_xlabel(r"$\tau$ [MPa]")
#ax2.set_xlabel("$\Pi$ [J]")
#ax1.set_xlim([0.0,None])
#ax1.set_ylim([layers[0][0],layers[-1][1]])
#ax2.set_xlim([0.0,None])
#ax2.set_ylim([layers[0][0],layers[-1][1]])
#ax1.set_yticks(np.arange(layers[0][0],layers[-1][1]+0.001, 1.0))
#ax2.set_yticks(np.arange(layers[0][0],layers[-1][1]+0.001, 1.0))
#ax2.axes.yaxis.set_ticklabels([])
#ax1.title.set_text(r'$\tau^{TB}$(Q) vs $\tau^{PS}$(Q)')
#ax2.title.set_text(r'$\Pi^{TB}$(Q) vs $\Pi^{PS}$(Q)')

#fig.subplots_adjust(bottom=0.2)
#labels = ["TB Original","TB Corrected","PS"]
#fig.legend(labels=labels, loc="lower center", ncol=3)
#plt.show()