import math

def sumar(a,b):
    return ( a[0] + b[0], a[1] + b[1] )

def restar(a,b):
    return ( a[0] - b[0], a[1] - b[1] )

def multiplicar(a,b):
    p = (a[0]*b[0])
    print(p)
    s = (a[1]*b[1])
    print(s)
    t = (a[0]*b[1])
    print(t)
    c = (b[0]*a[1])
    print(c)
    primero = p - s
    segundo = t + c
    return (primero,segundo)

def dividir(a,b):
    p = (a[0]*b[0]) + (a[1]*b[1])
    print(p)
    s = (b[0]*a[1]) - (a[0]*b[1])
    print(s)
    t = (b[0]**2) + (b[1]**2)
    print(t)
    primero = int(p/t)
    segundo = int(s/t)
    return (primero , segundo)

def modulo(a):
    return  int(((a[0]**2 + a[1]**2))**0.5)

def conjugado(a):
    return ( a[0], -a[1] )

def PolarCartesiano(a):
    c = (a[0]*math.cos(a[1]))
    d = (a[0]*math.sin(a[1]))
    rad1 = round(math.radians(c))
    rad2 = round(math.radians(d))
    return rad1 , rad2

def CartesianoPolar(a):
    c = math.atan(a[1]/a[0])
    rad = math.radians(c)
    return (round(((a[0]**2) + (a[1]**2))**0.5) , round(rad))

def ComplextToString(c):
    return str(c[0]) + "+" + str(c[1]) + "i"