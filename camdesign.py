import numpy as np
import matplotlib.pyplot as plt

def Cicloidal(L,theta,beta,orientacion):
    if orientacion == "ascenso":
        resultado = L*((theta/beta) - (1/(2*np.pi)) * np.sin((2*np.pi*np.radians(theta))/np.radians(beta)))
    elif orientacion == "descenso":
        resultado = L*(1 - (theta/beta) + (1/(2*np.pi)) * np.sin((2*np.pi*np.radians(theta))/np.radians(beta)))
    else:
        resultado = "Orientación necesaria"
    return resultado

def ArmonicoSimple(L,theta,beta,orientacion):
    if orientacion == "ascenso":
        resultado = (L/2)*(1 - np.cos((np.pi*np.radians(theta))/np.radians(beta)))
    elif orientacion == "descenso":
        resultado = (L/2)*(1 + np.cos((np.pi*np.radians(theta))/np.radians(beta)))
    else:
        resultado = "Orientación necesaria"
    return resultado