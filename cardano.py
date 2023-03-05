import math
import cmath

# def binomial (a, b, c):
#  delta = b*b-4*a*c
#  sqrdel = cmath.sqrt(delta)
#  x1 = (-b - sqrdel)/2*a
#  x2 = (-b + sqrdel)/2*a
#  print(x1,x2) 

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

def trinomial (a,b,c,d):
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

# print(binomial (1,2,1))
print(trinomial(1,1,1,1))
# print(trinomial(1,5,4,0))