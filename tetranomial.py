import math
import cmath
from cardano import binomialReal
from cardano import trinomialReal
from cardano import cbrt

def quadraticReal(a,b,c,d,e):
    # this if checks that equation is biquadratic where we can solve it just by simplify by t=x^2
    if(b==d and b ==0):
        result = binomialReal(a,c,e)
        if(result[0]>=0 and result[1]>=0):
            t0=math.sqrt(result[0])
            t1=-math.sqrt(result[0])
            t2=math.sqrt(result[1])
            t3=-math.sqrt(result[1])
            return t0,t1,t2,t3
        elif(result[0]>=0 and result[1]<0):
            t0=math.sqrt(result[0])
            t1=-math.sqrt(result[0])
            return t0,t1
        elif(result[1]>=0 and result[0]<0):
            t0=math.sqrt(result[1])
            t1=-math.sqrt(result[1])
            return t0,t1
        else:
            return "no real solutions"
    # this if checks that equation is quasi-symmetric iif yes we can simplify it by t=x+1/x
    elif(a==e and b==d):
        result = binomialReal(a,b,c-2*a)
        m1=result[0]
        m2=result[1]
        t1 = binomialReal(1,-m1,1)
        t2 = binomialReal(1,-m2,1)
        return t1,t2
    
    else:
        k=-3*b*b/8*a*a+c/a
        l=b*b*b/8*a*a*a-b*c/2*a*a+d/a
        m=-3*b*b*b*b/256*a*a*a*a+c*b*b/16*a*a*a-b*d/4*a*a+e/a
        p=-k*k/12-m
        q=-k*k*k/108+k*m/3-l*l/8
        w=cbrt(-q/2+math.sqrt(q*q/4+p*p*p/27))
        y=k/6+w-k/3*w
        t1=1/2( -math.sqrt(2*y-k) + math.sqrt(-2*y-k+2*l/math.sqrt(2*y-k)))
        t2=1/2( -math.sqrt(2*y-k) - math.sqrt(-2*y-k+2*l/math.sqrt(2*y-k)))
        t3=1/2(  math.sqrt(2*y-k) + math.sqrt(-2*y-k+2*l/math.sqrt(2*y-k)))
        t4=1/2(  math.sqrt(2*y-k) - math.sqrt(-2*y-k+2*l/math.sqrt(2*y-k)))
        return t1,t2,t3,t4



# print(quadraticReal(1,0,3,0,2))
print(quadraticReal(1,4,3,4,1))