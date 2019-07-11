import matplotlib.pyplot as plt 
import numpy as np 

vel=[0]
posy=[-1]
fgravedad=-9.8
dt=0.1
iteraciones=200

def aceleracion_T(fgravedad,posicion,vel):
	#se considera k=3 en el resorte
	aceleracion_P=fgravedad-(3*(posicion+1))
	if vel > 0:
		aceleracion_T=aceleracion_P-0.15*(vel**2)
	else:
		aceleracion_T=aceleracion_P+0.15*(vel**2)
	return aceleracion_T

def verlet (pos_actual,pos_anterior, aceleracion,deltaT):
	return (2*pos_actual)-pos_anterior+aceleracion*deltaT**2

def euler (pos_actual,vel_actual, aceleracion, deltaT):
	return pos_actual+vel_actual*deltaT+0.5*aceleracion*deltaT**2

def grafica(ejey):
	plt.clf()
	plt.ylim(-8,0)
	plt.plot(0,ejey, color='red',marker='o', linestyle='None')
	plt.pause(0.1)

def veli(vectorpos):
	velo=(vectorpos[-1]-vectorpos[-2])/dt
	return(velo)

plt.ion()
plt.figure()
grafica(posy[-1])

aceleracion=aceleracion_T(fgravedad,posy[-1],0)
posy.append(euler(posy[-1],0,aceleracion,dt))
vel.append(veli(posy))
grafica(posy[-1])

for i in range(iteraciones):
	aceleracion=aceleracion_T(fgravedad,posy[-1],vel[-1])
	posy.append(verlet(posy[-1],posy[-2],aceleracion,dt))
	vel.append(veli(posy))
	grafica(posy[-1])