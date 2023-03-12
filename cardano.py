import math
import cmath

# this is classic quadratic equation solver ax^2+bx+c=0 for real numbers
def binomialReal (a, b, c):
 delta = b*b-4*a*c
 if delta > 0:
    sqrdel = math.sqrt(delta)
    x1 = (-b - sqrdel)/2*a
    x2 = (-b + sqrdel)/2*a
    print(x1,x2)
 elif delta == 0:
    x0 = -b/2*a
    print(x0)
 else:
    print("no real solutions")
# print(binomialReal(1,1,1))

# this is like ^up but for complex numbers
def binomialComplex (a, b, c):
 delta = b*b-4*a*c
 sqrdel = cmath.sqrt(delta)
 x1 = (-b - sqrdel)/2*a
 x2 = (-b + sqrdel)/2*a
 print(x1,x2) 
# print(binomialComplex(1,1,1))

# this function is created due to python's problem with cube roots with negative numbers, instead of giving real solution it gives complex one (and of course wrong one)
def cbrt(a):
    if isinstance(a,complex):
       x = a.real
       y = a.imag
       z = math.sqrt(x*x+y*y)
       k = math.atan(y/x)
       a = z**(1/3) * math.cos(k/3) + z**(1/3) *  math.sin(k/3)*1j
       return a
    else:   
        if a >=0:
            a = a **(1/3)
            return a
        else:
            a = abs(a)
            a = a **(1/3)*-1
        return a
# print(cbrt(-27))
# print(cbrt(complex(1,1)))

# this is like quadratic equation but for ax^3+bx^2+cx+d=0 for real numbers (round is for making it better counts because of floating problems like 2/3=0.6666665)
def trinomialReal (a,b,c,d):
 p = c/a - b*b/3*a*a
 q = 2*b*b*b/27*a*a*a + d/a -b*c/3*a*a
 d = 1/4*q*q + 1/27*p*p*p
 d = round(d,6)
 if d > 0:
    x = round(cbrt(-q/2 - math.sqrt(d)) + cbrt(-q/2 + math.sqrt(d)) - b/3*a,2)
    return print(x)
 elif d == 0:
    x1 = round(cbrt(q/2) - b/3*a,2)
    x2 = round(-2*cbrt(q/2) - b/3*a,2)
    return print(x1,x2)
 else:
    phi = math.acos(-q/2 / math.sqrt(-p*p*p/27))
    x1 = round(2*math.sqrt(-p/3)*math.cos(phi/3) - b/3*a,2)
    x2 = round(2*math.sqrt(-p/3)*math.cos((phi+2*math.pi)/3) - b/3*a,2)
    x3 = round(2*math.sqrt(-p/3)*math.cos((phi+4*math.pi)/3) - b/3*a,2)
    return print(x1,x2,x3)

# print(trinomialReal(1,-1,1,-1))
# print(trinomialReal(1,2,1,0))
# print(trinomialReal(1,3,2,0))

# like ^up but for complex ones
def trinomialComplex (a,b,c,d):
 e1 = complex(-1/2,-cmath.sqrt(3)/2)
 e2 = complex(-1/2,cmath.sqrt(3)/2)
 p = c/a - b*b/3*a*a
 q = 2*b*b*b/27*a*a*a + d/a -b*c/3*a*a
 d = 1/4*q*q + 1/27*p*p*p
#  print(p)
#  print(q)
 u = cbrt( -q/2 + cmath.sqrt(d))
 print(u)
 v = -3*p/u
 print(v)
 z0 = u + v
 z1 = u*e1+v*e2
 z2 = u*e2+v*e1
 print(z0)
 print(z1)
 print(z2)
#  print(p)
#  print(z0*z1+z0*z2+z1*z2)

# # print(binomial (1,2,1))
# print(trinomialComplex(1,1,1,1))
# # print(trinomial(1,5,4,0))