from math import *
ro = 200/pi

from utils import *

#Horizontal Curve
# T=R*Tan(Delta/2)
# D=R*Delta/ro
# E=R/cos(Delta/2)-R

R = float(input("R= "))
Delta=float(input("Delta= "))
T=round(R*tang(Delta/2),3)
D=round(R*Delta/ro,3)
E=round(R/cosg(Delta/2)-R,3)
print("T= ",T)
print("D= ",D)
print("E= ",E)
