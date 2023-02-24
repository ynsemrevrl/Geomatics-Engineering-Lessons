from math import *
ro = 200/pi

def triangle(x1,x2):
    return round(200-(x1+x2),4)

def sing(angle):
    return sin(angle/ro)

def cosg(angle):
    return cos(angle/ro)

def tang(angle):
    return tan(angle/ro)

def cotg(angle):
    return 1/tan(angle/ro)

def atang(radian):
    return round(atan(radian)*ro,4)

def azimuth_S(x1,y1,x2,y2):
    dy = round(y2-y1,3)
    dx = round(x2-x1,3)
    dd = dy/dx
    S = round((dy**2+dx**2)**(1/2),3)
    if dy>0 and dx>0:
        return atang(dd),S,dy,dx
    elif dy>0 and dx<0:
        return atang(dd)+200,S,dy,dx
    elif dy<0 and dx<0:
        return atang(dd)+200,S,dy,dx
    else:
        return atang(dd)+400,S,dy,dx
    
def tangent_theorem(p1,p2,p3,p4):  
    x = atang((cotg(p1)+cotg(p2)+cotg(p3)+cotg(p4))/(cotg(p1)*cotg(p3)-cotg(p2)*cotg(p4)))
    if x < 0:
        return x + 200
    else:
        return x
    
def sine_theorem(x,alfa,beta,delta,S):
    a = triangle(beta,x)
    b = triangle(alfa,200-x)
    d = triangle(delta,200-x)
    s1 = round(sing(b)*S/sing(alfa+beta),3)
    s2 = round(sing(a)*S/sing(alfa+beta),3)
    s3 = round(sing(delta)*s1/sing(a+d),3)
    return a,b,d,s1,s2,s3

def bp1_azimuth(a,BA):
    if 400-a > BA:
        return BA+a
    else:
        return BA-200-(200-a)

def p1p2_azimuth(x,BA):
    if x < BA:
        return BA - x
    else:
        return BA+400-x
    
def polygon(x1,y1,s,a):
    x = x1 + s*cong(a)
    y = y1 + s*sing(a)
    return x,y

def refraction_azimuth(a,b):
    q = round(a+ b,4)
    if q < 200:
        return q+200
    elif q >= 200 and q<=600:
        return q-200
    else:
        return q-600
