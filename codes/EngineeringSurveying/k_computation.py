from math import *

ρ = 200/pi
def gr(grad):
    radian = grad * pi / 200
    return radian

def rg(radian):
    grad = radian * 200 / pi
    return grad

def cot(x):
    return 1/tan(gr(x))

def kh(R,S,Za,Zb):
    """
             R     Za+Zb-200
    k = 1 - --- × -----------
             S         ρ
    """
    R = float(input("How many meters is R?: "))
    S = float(input("How many meters is S?: "))
    Za = float(input("How many grad is Za(Vertical angle for A)?: "))
    Zb = float(input("How many grad is Zb(Vertical angle for B)?: "))
    
    k = 1 - (R/S) * ((Za + Zb - 200) / ρ)
    
    print("k = %0.3f" %(k))
    return k
