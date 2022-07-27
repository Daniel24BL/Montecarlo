import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Leemos los datos que contiene el Data set con el que estamos trabajando.
Datos1b= pd.read_excel('../tabla1b.xlsx')
Datos1b

# desplegamos los datos de los 5 primeros registros
demanda.head()

demandas = demanda.groupby("Prob")
demandas.sum()

# Obtenemos la media de cada uno de las frecuencias
demandas.mean()
tot = demandas.mean()
tot

# Ordenamos por Día
suma = tot['Número de días de alquiler por auto'].sum()
n=len(tot)
suma
x1 = tot.assign(Probabilidad=lambda x: x['Número de días de alquiler por auto'] / suma)
x2 = x1.sort_values('Prob')
a=x2['Probabilidad']
a

a1= np.cumsum(a)     #Cálculo la suma acumulativa de las probabilidades
x2['ProbabilidadAcum'] =a1
x2

x2['Min'] = x2['ProbabilidadAcum']
x2['Max'] = x2['ProbabilidadAcum']
x2

lis = x2["Min"].values
lis2 = x2['Max'].values
lis[0]= 0
for i in range(1,4):
    lis[i] = lis2[i-1]
    print(i,i-1)
x2['Min'] = lis
x2

n, m, a, x0, c = 15, 2**32, 22695477, 4, 1
x = [1] * n
r = [0.1] * n
for i in range(0, n):
    x[i] = ((a*x0)+c) % m
    x0 = x[i]
    r[i] = x0 / m
# llenamos nuestro DataFrame
d = {'ri': r }
dfMCL = pd.DataFrame(data=d)
dfMCL

def busqueda(arrmin, arrmax, valor):
    #print(valor)
    for i in range (len(arrmin)):
        # print(arrmin[i],arrmax[i])
        if valor >= arrmin[i] and valor <= arrmax[i]:
            return i
            print(i)
    return -1

xpos = dfMCL['ri']
posi = [0] * n
print (n)
for j in range(n):
    val = xpos[j]
    pos = busqueda(min,max,val)
    posi[j] = pos
    
x2 = x2.astype({"Número de días de alquiler por auto" : int})
x2

import itertools
import math
simula = []
for j in range(n):
    for i in range(n):
        sim = x2.loc[x2["Número de días de alquiler por auto"] == posi[i]+1]
        simu = sim.filter(['Probabilidad']).values
        iterator = itertools.chain(*simu)
        for item in iterator:
            a=item
            simula.append(round(a,2))
simula

dfMCL["Simulación"] = pd.DataFrame(simula) 
dfMCL["cantidad de autos que debería comprar la compañía"] = dfMCL["Simulación"] * 15
dfMCL