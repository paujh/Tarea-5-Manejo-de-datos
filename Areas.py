#Jorge Hinostrosa Paula 
#Haremos un programa que calcule areas de 5 figuras
import math as m

def ACirculo(x):
  return m.pi*(x**2)

def AAro(x,y):
  return m.pi*(x**2)-m.pi*(y**2)

def ACuadrado(x):
  return x*x

def ATriangulo(x,y):
  return (x*y)/2

def ARectangulo(x,y):
  return x*y
