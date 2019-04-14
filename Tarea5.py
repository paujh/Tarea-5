#Jorge Hinostrosa Paula
#paulajhinostrosa@ciencias.unam.mx

import random as r

class MatrizNN:
  def __init__(self,N,matriz):
    self.N=N
    self.matriz=matriz

  def __str__(self):
    cadena=""
    for i in range(self.N):
      cadena=cadena+str(self.matriz[i])+"\n"
    return cadena
  
  def cerosNN(n):
    matrizceros=[[0 for i in range (n)]for j in range(n)]
    return MatrizNN(n,matrizceros)
  
  def identidadNN(n):
    matrizidentidad=[]
    for i in range(n):
	    fila=[]
	    for j in range(n):
		    valor=1 if i==j else 0
		    fila.append(valor)
	    matrizidentidad.append(fila)
    return MatrizNN(n,matrizidentidad)
  
  def aleatoriaNN(n):
    matrizaleatoria=[]
    for i in range(n):
      matrizaleatoria.append([r.randint(0,9) for i in range(n)])
    return MatrizNN(n,matrizaleatoria)

  def __add__ (M,N):
    suma=M
    if M.N==N.N: 
      for i in range(M.N):
        for j in range(M.N):
          suma.matriz[i][j]=M.matriz[i][j]+N.matriz[i][j]
      return suma
    else:
      return ("La longitud de las matrices no coincide")
  
  def __sub__(M,N):
    resta=M 
    if M.N==N.N: 
      for i in range(M.N):
        for j in range(M.N):
          resta.matriz[i][j]=M.matriz[i][j]-N.matriz[i][j]
      return resta 
    else:
      return ("La longitud de las matrices no coincide")

  def __mul__(M,n):
    mul=M 
    for i in range(M.N):
      for j in range(M.N):
        mul.matriz[i][j]=M.matriz[i][j]*n
    return mul 

m1=MatrizNN(3,[[1,9,6],[3,5,8],[2,6,1]])
print(m1)
m2=MatrizNN.cerosNN(5)
print(m2)
m3=MatrizNN.identidadNN(8)
print(m3)
m4=MatrizNN.aleatoriaNN(5)
print(m4)
m5=MatrizNN(3,[[1,4,5],[2,5,9],[1,1,1]])
m6=m1+m5
print(m6)
m7=m1+m2
print(m7)
m8=m5-m5
print(m8)
m9=m1-m2
print(m9)
m10=MatrizNN(4,[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
m11=m10*3
print(m11)
