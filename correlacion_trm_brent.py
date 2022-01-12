#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 21:47:28 2021
Correlación entre TRM y Brent
Autor: Carlos Armando De Castro (cadecastro.com)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
corte=int(input('Año de corte (mayor que 1992): '))
#DATOS PETRÓLEO:
petroleo=pd.read_csv('https://datasource.kapsarc.org/explore/dataset/spot-prices-for-crude-oil-and-petroleum-products/download/?format=csv&timezone=America/Bogota&lang=en&use_labels_for_header=true&csv_separator=%3B',sep=';',usecols=['Date','Brent Spot Price (U.S. Dollars per Barrel)'])
petroleo['Date']=pd.to_datetime(petroleo['Date'],yearfirst=True)
petroleo=petroleo.rename(columns={'Date':'Fecha','Brent Spot Price (U.S. Dollars per Barrel)':'Brent'})
petroleo=petroleo.sort_values(by='Fecha',ascending=True)
petroleo['Año']=pd.DatetimeIndex(petroleo['Fecha']).year
petroleo=petroleo.drop(petroleo[petroleo['Año']<corte].index)
#DATOS DE LA TRM:
trm=pd.read_csv('https://www.datos.gov.co/api/views/32sa-8pi3/rows.csv',usecols=['VALOR','VIGENCIADESDE'])
trm['VIGENCIADESDE']=pd.to_datetime(trm['VIGENCIADESDE'],dayfirst=True)
trm=trm.sort_values(by='VIGENCIADESDE',ascending=True)
trm['Año']=pd.DatetimeIndex(trm['VIGENCIADESDE']).year
trm=trm.drop(trm[trm['Año']<corte].index)
trm=trm.rename(columns={'VIGENCIADESDE':'Fecha','VALOR':'TRM'})
#Combinar bases de datos:
bd=trm.merge(petroleo,on='Fecha',how='inner')
bd=bd.drop(columns='Año_x')
bd=bd.rename(columns={'Año_y':'Año'})
bd=bd.dropna()
bd['Var Porc TRM']=bd['TRM'].pct_change(periods=1,fill_method='pad')
bd['Var Porc Brent']=bd['Brent'].pct_change(periods=1,fill_method='pad')
bd.set_index('Fecha', inplace=True)
del trm, petroleo
#Regresión Brent vs. TRM
d_brent=np.polyfit(bd['Brent'],bd['TRM'],1)
f_brent = np.poly1d(d_brent)
bd.insert(4,'Regresion TRM Brent',f_brent(bd['Brent']))
#Regresión variaciones porcentuales:
#d_v=np.polyfit(bd['Var Porc Brent'],bd['Var Porc TRM'],1)
#f_v = np.poly1d(d_v)
bd.insert(5,'Regresion variaciones',f_brent(bd['Var Porc Brent']))
#GRÁFICAS:
plt.figure(1,figsize=(12,8))
plt.subplot(211)
plt.plot(bd.index,bd['TRM'],'b.')
plt.plot(bd.index,bd['TRM'].rolling(window=15).mean(),'r')
plt.grid(True,'both','both')
plt.legend(['Datos','Media móvil 15 días'])
plt.ylabel('TRM')
plt.title('Series de tiempo')
plt.subplot(212)
plt.plot(bd.index,bd['Brent'],'b.')
plt.plot(bd.index,bd['Brent'].rolling(window=15).mean(),'r')
plt.grid(True,'both','both')
plt.legend(['Datos','Media móvil 15 días'])
plt.ylabel('Precio Brent')
plt.xlabel('cadecastro.com')
plt.figure(2,figsize=(12,8))
plt.subplot(211)
plt.plot(bd.index,bd['Var Porc TRM'],'b.')
plt.plot(bd.index,bd['Var Porc TRM'].rolling(window=15).mean(),'r')
plt.grid(True,'both','both')
plt.legend(['Datos','Media móvil 15 días'])
plt.ylabel('Var. Porc. TRM')
plt.title('Series de tiempo')
plt.subplot(212)
plt.plot(bd.index,bd['Var Porc Brent'],'b.')
plt.plot(bd.index,bd['Var Porc Brent'].rolling(window=15).mean(),'r')
plt.grid(True,'both','both')
plt.legend(['Datos','Media móvil 15 días'])
plt.ylabel('Var Porc Brent')
plt.xlabel('cadecastro.com')
plt.figure(3,figsize=(12,8))
plt.plot(bd['Brent'],bd['TRM'],'b.')
plt.plot(bd['Brent'],bd['Regresion TRM Brent'],'r')
plt.ylabel('TRM')
plt.xlabel('Precio Brent')
plt.title('TRM vs. Brent',loc='left')
plt.title('cadecastro.com',loc='right')
plt.figure(4,figsize=(12,8))
plt.plot(bd['Var Porc Brent'],bd['Var Porc TRM'],'b.')
#plt.plot(bd['Var Porc Brent'],bd['Regresion variaciones'],'r')
plt.ylabel('Var. Porc. TRM')
plt.xlabel('Var. Porc. Brent')
plt.title('Var. Porc. TRM vs. Var. Porc. Brent',loc='left')
plt.title('cadecastro.com',loc='right')