import matplotlib.pyplot as plt 
import numpy as np 

posy=[-1]
fgravedad=-9.8
dt=0.1
iteraciones=100

def aceleracion_T(fgravedad,posicion):
	#se considera k=3 en el resorte
	aceleracion_T=fgravedad-(3*(posicion+1))
	return aceleracion_T

def verlet (pos_actual,pos_anterior, aceleracion,deltaT):
	return (2*pos_actual)-pos_anterior+aceleracion*deltaT**2

def euler (pos_actual,vel_actual, aceleracion, deltaT):
	return pos_actual+vel_actual*deltaT+0.5*aceleracion*deltaT**2

plt.ion()
plt.figure()
plt.ylim(-8,0)
plt.plot(0,posy[-1], color='red',marker='o', linestyle='None')
plt.pause(0.1)

aceleracion=aceleracion_T(fgravedad,posy[-1])
posy.append(euler(posy[-1],0,aceleracion,dt))
plt.clf()
plt.ylim(-8,0)
plt.plot(0,posy[-1], color='red',marker='o', linestyle='None')
plt.pause(0.1)

for i in range(iteraciones):
	aceleracion=aceleracion_T(fgravedad,posy[-1])
	posy.append(verlet(posy[-1],posy[-2],aceleracion,dt))
	plt.clf()
	plt.ylim(-8,0)
	plt.plot(0,posy[-1], color='red',marker='o', linestyle='None')
	plt.pause(0.1)
