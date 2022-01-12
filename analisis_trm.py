#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 21:24:02 2021
ANÁLISIS PRECIO DEL DÓLAR EN COLOMBIA
Autor: Carlos Armando De Castro (cadecastro.com)
"""
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
corte=int(input('Año de corte: '))
#Importar datos de Datos Abiertos Colombia:
trm=pd.read_csv('https://www.datos.gov.co/api/views/32sa-8pi3/rows.csv',usecols=['VALOR','VIGENCIADESDE'])
#Conversión de fechas:
trm['VIGENCIADESDE']=pd.to_datetime(trm['VIGENCIADESDE'],dayfirst=True)
#Reorganizar por fecha de más antiguo a más reciente:
trm=trm.sort_values(by='VIGENCIADESDE',ascending=True)
#Quitar años anteriores a 2018:
trm['Año']=pd.DatetimeIndex(trm['VIGENCIADESDE']).year
#Fecha como index de la serie:
trm=trm.drop(trm[trm['Año']<corte].index)
#Agregar columna de diferencia porcentual:
trm['Variación porcentual']=trm['VALOR'].pct_change(periods=1,fill_method='pad')
#Agregar columna fecha numérica:
trm['Fecha numerica']=trm['VIGENCIADESDE'].map(dt.datetime.toordinal)
trm.set_index('VIGENCIADESDE', inplace=True)
trm=trm.drop_duplicates(subset='Fecha numerica')
#Regresión lineal:
d=np.polyfit(trm['Fecha numerica'],trm['VALOR'],1)
f= np.poly1d(d)
trm.insert(4,'Reg Lineal',f(trm['Fecha numerica']))
print('Último cierre el ',trm.index[len(trm['VALOR'])-1],'es con TRM = ',trm['VALOR'][len(trm['VALOR'])-1])
#Gráficas:
plt.figure(1,figsize=(12,6))
plt.plot(trm.index,trm['VALOR'],'b.')
plt.plot(trm.index,trm['VALOR'].rolling(window=7).mean(),'y')
plt.plot(trm.index,trm['VALOR'].rolling(window=15).mean(),'r')
plt.plot(trm.index,trm['Reg Lineal'],'g')
plt.title('Precio del dólar en Colombia',loc='left')
plt.title('cadecastro.com',loc='right')
plt.ylabel('COP/USD')
plt.grid(True,which='both',axis='both')
plt.legend(['TRM día','Media móvil semanal','Media móvil 15 días','Reg. lineal'])
plt.figure(2,figsize=(12,6))
plt.plot(trm.index,trm['Variación porcentual'],'b.')
plt.plot(trm.index,trm['Variación porcentual'].rolling(window=7).mean(),'y')
plt.plot(trm.index,trm['Variación porcentual'].rolling(window=15).mean(),'r')
plt.title('Variación porcentual precio dólar Colombia',loc='left')
plt.title('cadecastro.com',loc='right')
plt.ylabel('COP/COP')
plt.grid(True,which='both',axis='both')
plt.legend(['Var. Porc. día','Media móvil semanal','Media móvil 15 días'])
plt.figure(3,figsize=(12,6))
plt.plot(trm['VALOR'][len(trm['VALOR'])-7:],'bo-')
plt.title('TRM última semana',loc='left')
plt.title('cadecastro.com',loc='right')
plt.ylabel('COP/USD')
plt.grid(True,which='both',axis='both')
plt.legend(['TRM día','Media móvil 3 días'])