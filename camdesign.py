import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

def CicloidalT(L,theta,beta,orientacion,derivada = 0):
    if derivada == 0:
        if orientacion == "ascenso":
            resultado = L*((theta/beta) - (1/(2*np.pi)) * np.sin((2*np.pi*theta)/beta))
        elif orientacion == "descenso":
            resultado = L*(1 - (theta/beta) + (1/(2*np.pi)) * np.sin((2*np.pi*theta)/beta)) 
    elif derivada == 1:
        if orientacion == "ascenso":
            resultado = (L/beta)*(1 - np.cos((2*np.pi*theta/beta)))
        elif orientacion == "descenso":
            resultado = - (L/beta)*(1 - np.cos((2*np.pi*theta/beta)))
    elif derivada == 2:
        if orientacion == "ascenso":
            resultado = (2*np.pi*L/beta**2)*np.sin((2*np.pi*theta)/beta)
        elif orientacion == "descenso":
            resultado = - (2*np.pi*L/beta**2)*np.sin((2*np.pi*theta)/beta)
    elif derivada == 3:
        if orientacion == "ascenso":
            resultado = (4*(np.pi**2)*L/beta**3)*np.cos((2*np.pi*theta)/beta)
        elif orientacion == "descenso":
            resultado = - (4*(np.pi**2)*L/beta**3)*np.cos((2*np.pi*theta)/beta)
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

def CoordADAMS(radio,theta,ruta = './CoordADAMS.csv'):
    x = []
    y = []
    z = np.zeros((362))
    for t,r in zip(theta,radio):
        aux = r*np.cos(np.radians(t))
        x.append(aux)
        aux = r*np.sin(np.radians(t))
        y.append(aux)

    x.append(radio[0]*np.cos(np.radians(theta[0])))
    y.append(radio[0]*np.sin(np.radians(theta[0])))

    df_coord = pd.DataFrame({'X':x,
                             'Y':y,
                             'Z':z})
    df_coord.to_csv(ruta, index=False, header=False)

def CoordINVENTOR(radio,theta,ruta = './CoordINVENTOR.csv'):
    x = []
    y = []
    for t,r in zip(theta,radio):
        aux = r*np.cos(np.radians(t))
        x.append(aux)
        aux = r*np.sin(np.radians(t))
        y.append(aux)

    df_coord = pd.DataFrame({'X':x,
                             'Y':y})
    df_coord.to_csv(ruta, index=False, header=False)