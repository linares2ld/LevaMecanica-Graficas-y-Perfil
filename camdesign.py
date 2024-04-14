import numpy as np
import matplotlib.pyplot as plt

def Cicloidal(L,theta,beta,orientacion,derivada = 0):
    if derivada == 0:
        if orientacion == "ascenso":
            resultado = L*((theta/beta) - (1/(2*np.pi)) * np.sin((2*np.pi*np.radians(theta))/np.radians(beta)))
        elif orientacion == "descenso":
            resultado = L*(1 - (theta/beta) + (1/(2*np.pi)) * np.sin((2*np.pi*np.radians(theta))/np.radians(beta))) 
    elif derivada == 1:
            if orientacion == "ascenso":
                resultado = (L/np.radians(beta))*(1 - np.cos((2*np.pi*np.radians(theta))/np.radians(beta)))
            elif orientacion == "descenso":
                resultado = - (L/np.radians(beta))*(1 - np.cos((2*np.pi*np.radians(theta))/np.radians(beta)))
    elif derivada == 2:
            if orientacion == "ascenso":
                resultado = (2*np.pi*L/np.radians(beta)**2)*np.sin((2*np.pi*np.radians(theta))/np.radians(beta))
            elif orientacion == "descenso":
                resultado = - (2*np.pi*L/np.radians(beta)**2)*np.sin((2*np.pi*np.radians(theta))/np.radians(beta))         
    return resultado

def ArmonicoSimple(L,theta,beta,orientacion,derivada=0):
    if derivada == 0:
        if orientacion == "ascenso":
            resultado = (L/2)*(1 - np.cos((np.pi*np.radians(theta))/np.radians(beta)))
        elif orientacion == "descenso":
            resultado = (L/2)*(1 + np.cos((np.pi*np.radians(theta))/np.radians(beta)))
    elif derivada == 1:
        if orientacion == "ascenso":
            resultado = (np.pi*L/2*np.radians(beta))*np.sin((np.pi*np.radians(theta))/np.radians(beta))
        elif orientacion == "descenso":
            resultado = - (np.pi*L/2*np.radians(beta))*np.sin((np.pi*np.radians(theta))/np.radians(beta))
    elif derivada == 2:
        if orientacion == "ascenso":
            resultado = ((np.pi**2)*L/2*np.radians(beta)**2)*np.cos((np.pi*np.radians(theta))/np.radians(beta))
        elif orientacion == "descenso":
            resultado = - ((np.pi**2)*L/2*np.radians(beta)**2)*np.cos((np.pi*np.radians(theta))/np.radians(beta))
    return resultado