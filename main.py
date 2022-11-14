import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
from sympy import *
from os import system
system("clear")

pprint("hola")

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

# Plot VM for Sx and Sy

replacements = [(Sz,0),(Sxy,0),(Sxz,0),(Syz,0),(YT,10)]

VM1 = simplify(VM.subs(replacements))

A = solve(VM1, Sy, dict=true)

Sxmax = solve(A[0][Sy], Sx)[0]
Sxmin = solve(A[1][Sy], Sx)[0]

SxPos = np.arange(0,Sxmax,0.1)
SxPos = np.append(SxPos,Sxmax)
SxNeg = np.arange(0,Sxmin,-0.1)
SxNeg = np.append(SxNeg,Sxmin)

SyPosPos = []
SyPosNeg = []
for i in SxPos:
    SyPosPos.append(-A[0][Sy].subs(Sx,i))
    SyPosNeg.append(A[0][Sy].subs(Sx,i))

SyNegPos = []
SyNegNeg = []
for i in SxNeg:
    SyNegPos.append(A[1][Sy].subs(Sx,i))
    SyNegNeg.append(-A[1][Sy].subs(Sx,i))



#p1 = plot_implicit(Eq(Sx**2+Sy**2-Sx*Sy-100, 0),(Sx, -12, 12), (Sy, -12, 12), adaptive=False)

p1 = plot_implicit(Eq(VM1, 0),(Sx, -12, 12), (Sy, -12, 12), adaptive=False)

#fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))
fig, ax1 = plt.subplots()
ax1.title.set_text('Von Mises')
ax1.set_ylabel("Sy")
ax1.set_xlabel("Sx")
#TBTTauCorrected = [num*factorK for num in TBTTau]
ax1.plot(SxPos, SyPosPos, label = "line 1", linestyle=":", color="tab:orange")
ax1.plot(SxPos, SyPosNeg, label = "line 1", linestyle=":", color="tab:orange")
ax1.plot(SxNeg, SyNegPos, label = "line 1", linestyle=":", color="tab:orange")
ax1.plot(SxNeg, SyNegNeg, label = "line 1", linestyle=":", color="tab:orange")
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

fig.subplots_adjust(bottom=0.2)
labels = ["TB Original","TB Corrected","PS"]
fig.legend(labels=labels, loc="lower center", ncol=3)
plt.show()