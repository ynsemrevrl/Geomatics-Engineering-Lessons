from math import *

def gr(grad):
    """
    from grad to radian
    """
    radian = grad * pi / 200
    return radian

def rg(radian):
    """
    from radian to  grad
    """
    grad = radian * 200 / pi
    return grad

def cot(x):
    return 1/tan(gr(x))

print("""Trigonometric Levelling Calculation
*****************************
For short distance(S<250m) : 1
For long distance(S>250m)  : 2
___________________________________________________________________________________""")
operationKvU = input("Do you want to run which operation?: ") #short or long distance operation selection
print("___________________________________________________________________________________")
if operationKvU == "1":
    print("""\nFor measurement with a short distance from a single point;
                    If S length can be measured          : 1
                    If S length cannot be measured       : 2
                    If S will be measured with two plane : 3""")
    operationSvN = input("""                    Please, select an operation.              : """) #X-dependent process selection
    print("___________________________________________________________________________________")
    if operationSvN == "1":
        opSvN2 = input("""Ht' verilmişse 1
  verilmemişse 2:""")
        print("___________________________________________________________________________________")
        if opSvN2 == "1":
            Ha = float(input("Enter Ha height.          : "))
            Z1 = float(input("Enter Z vertical angle.   : "))
            S = float(input("Enter S lenght.           : "))
            i = float(input("Enter tool height.        : "))
            Ht_ = float(input("Enter Ht' height.         : "))
            Ht = Ha + i + S / tan(gr(Z1))
            h = Ht - Ht_
            print("___________________________________________________________________________________")
            print("""\nHt = Ha + i + S.cot(z1)
Ht = {} m

h = Ht - Ht' = S(cotZ1 - cotZ2)
h = {} m""".format(Ht, h))
            
        elif opSvN2 == "2":
            Ha = float(input("Enter Ha height.          : "))
            Z1 = float(input("Enter Z1 vertical angle.  : "))
            Z2 = float(input("Enter Z2 vertical angle.  : "))
            S = float(input("Enter S lenght.           : "))
            i = float(input("Enter tool height.        :"))
            Ht = Ha + i + S * cot(Z1)
            Ht_ = Ha + i + S * cot(Z2)
            h = Ht - Ht_
            print("___________________________________________________________________________________")
            print("""\nHt = Ha + i + S.cot(z1)
Ht = {} m

Ht' = Ha + i + S.cot(Z2)
Ht' = {} m

h = Ht - Ht' = S(cotZ1 - cotZ2)
h = {} m""".format(Ht, Ht_, h))
    elif operationSvN == "2": #used variables α , β , γ , δ
        a = float(input("Enter a distance.        :"))
        b = float(input("Enter b distance.        :"))
        Z = float(input("Enter Z vertical angle.  : "))
        i = float(input("Enter tool height.       :"))
        Ha = float(input("Enter Ha height.         : "))
        Ht_ = float(input("Enter Ht' height.        : "))
        print("___________________________________________________________________________________")
        α = float(input("Enter α angle. : "))
        β = float(input("Enter β angle. : "))
        γ = float(input("Enter γ angle. : "))
        δ = float(input("Enter δ angle. : "))
        
        S1 = a * (sin(gr(α))/sin(gr(α + β)))
        S2 = b * (sin(gr(δ))/sin(gr(γ + δ)))
        S = (S1+S2)/2
        print("___________________________________________________________________________________")
        print("Calculated S with a= {}".format(S1))
        print("Calculated S with b= {}".format(S2))
        print("             Mean S= {}".format(S))
        print("___________________________________________________________________________________")
        Ht = Ha + i + S / tan(gr(Z))
        h = Ht - Ht_
        print("""\nHt = Ha + i + S.cot(z1)
Ht = {} m

h = Ht - Ht' = S(cotZ1 - cotZ2)
h = {} m""".format(Ht, h))
    else:
        Za = float(input("Enter Za vertical angle. : "))
        Zb = float(input("Enter Zb vertical angle. : "))
        Ha = float(input("Enter Ha height.         : "))
        Hb = float(input("Enter Hb height.         : "))
        Ht_ = float(input("Enter Ht' height.        : "))
        print("___________________________________________________________________________________")
        ia = float(input("Enter ia height.  :"))
        ib = float(input("Enter ib height.  :"))
        d = float(input("Enter d distance. :"))
        print("___________________________________________________________________________________")
        e = (Hb-Ha+ib-ia-d*cot(Za))/(cot(Za)-cot(Zb))
        Ht1 = Ha + ia + (d + e) * cot(Za)
        Ht2 = Hb + ib + e * cot(Zb)
        Ht = (Ht1+Ht2)/2
        h = Ht - Ht_
        print("e= {}m".format(e))
        print("___________________________________________________________________________________")
        print("Computation   → Ht= {}m".format(Ht1))
        print("Control       → Ht= {}m".format(Ht2))
        print("___________________________________________________________________________________")
        print("Ht= {}m".format(Ht))
        print("___________________________________________________________________________________")
        print("h= {}m".format(h))
        
