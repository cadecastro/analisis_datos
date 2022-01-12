#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PRECIO BRENT
Autor: Carlos Armando De Castro (cadecastro.com)
"""
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
petroleo=petroleo.drop(columns='Año')
petroleo=petroleo.set_index('Fecha')
petroleo=petroleo.sort_index()
print('Último cierre el ',petroleo.index[len(petroleo)-1],'es USD/barril = ',petroleo['Brent'][len(petroleo)-1])
#GRÁFICAS:
plt.figure(1)
plt.plot(petroleo.index,petroleo,'b.')
plt.plot(petroleo.index,petroleo.rolling(window=7).mean(),'r')
plt.grid(True,'both','both')
plt.legend(['Datos','Media móvil 7 días'])
plt.ylabel('USD/barril Brent')
plt.xlabel('cadecastro.com')
plt.figure(2)
plt.plot(petroleo[len(petroleo)-31:],'bo-')
plt.grid(True,'both','both')
plt.title('Precio Brent últimos 30 datos')
plt.ylabel('USD/Brent')