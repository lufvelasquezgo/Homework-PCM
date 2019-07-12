import matplotlib.pyplot as plt 
import numpy as np 

posx=[5]
dt=0.1
iteraciones=100

def aceleracion_T(posicion):
	#se considera k=3 en el resorte
	aceleracion_T=-(3*(posicion))
	return aceleracion_T

def verlet (pos_actual,pos_anterior, aceleracion,deltaT):
	return (2*pos_actual)-pos_anterior+aceleracion*deltaT**2

def euler (pos_actual,vel_actual, aceleracion, deltaT):
	return pos_actual+vel_actual*deltaT+0.5*aceleracion*deltaT**2

def grafica(ejex):
	plt.clf()
	plt.xlim(-6,6)
	plt.plot(ejex,0, color='blue',marker='o', linestyle='None')
	plt.pause(0.1)

plt.ion()
plt.figure()
grafica(posx[-1])

aceleracion=aceleracion_T(posx[-1])
posx.append(euler(posx[-1],0,aceleracion,dt))
grafica(posx[-1])

for i in range(iteraciones):
	aceleracion=aceleracion_T(posx[-1])
	posx.append(verlet(posx[-1],posx[-2],aceleracion,dt))
	grafica(posx[-1])