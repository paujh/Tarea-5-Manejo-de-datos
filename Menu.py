#Jorge Hinostrosa Paula 
#Haremos un programa que imprima un menu, y de acuerdo a la opcion que el usuario seleccione, sera el area que se calcule e imprima, usando el programa ya creado para calcular areas anteriormente. 
from Areas import*

print ("Menu", "\n", "1) Circulo", "\n", "2) Aro", "\n", "3) Cuadrado", "\n" ,"4) Triangulo", "\n", "5) Rectangulo", "\n", "6) Salir")

a = float(input("Escriba el numero de opcion que desea: "))

if a==1:
  x = float(input("Ingrese Radio: "))
    print ("El Area del circulo es:" + str(ACirculo(x)))
    a = float(input("Selecione Opcion: "))
elif a==2:
  x = float(input("Ingrese Radio Mayor: "))
  y = float(input("Ingrese Radio Menor: "))
  print ("El Area del aro es:" + str(AAro(x,y)))
  a = float(input("Selecione Opcion: "))
elif a==3:
  x = float(input("Ingrese un lado\n"))
  print ("El Area del cuadrado es:" + str(ACuadrado(x)))
  a = float(input("Selecione Opcion: "))
elif a==4:
  x = float(input("Ingrese Base: "))
  y = float(input("Ingrese Altura: "))
  print ("El Area del triangulo es:" + str(ATriangulo(x,y)))
  opc = float(input("Selecione Opcion: "))
elif a==5:
  x = float(input("Ingrese Base: "))
  y = float(input("Ingrese Altura: "))
  print ("El Area del Rectangulo es:" + str(ARectangulo(x,y)))
  a = float(input("Selecione Opcion: "))  
elif a==6:
  print("Adios.")
else: 
  print("Opcion incorrecta, intente de nuevo.")
