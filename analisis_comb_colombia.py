#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 09:12:18 2021
ANÁLISIS PRECIOS COMBUSTIBLES COLOMBIA
Autor: Carlos Armando De Castro (cadecastro.com)
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
datos_comb=pd.read_csv('https://www.datos.gov.co/api/views/7pcy-5vx9/rows.csv',usecols=['periodo','mes','municipio','producto','precio'])
datos_comb['mes']=datos_comb['mes'].replace(to_replace='Enero',value=1)
datos_comb['mes']=datos_comb['mes'].replace(to_replace='Febrero',value=2)
datos_comb['mes']=datos_comb['mes'].replace(to_replace='Marzo',value=3)
datos_comb['mes']=datos_comb['mes'].replace(to_replace='Abril',value=4)
datos_comb['mes']=datos_comb['mes'].replace(to_replace='Mayo',value=5)
datos_comb['mes']=datos_comb['mes'].replace(to_replace='Junio',value=6)
datos_comb['mes']=datos_comb['mes'].replace(to_replace='Julio',value=7)
datos_comb['mes']=datos_comb['mes'].replace(to_replace='5',value=5)
datos_comb['mes']=datos_comb['mes'].replace(to_replace='6',value=6)
datos_comb['mes']=datos_comb['mes'].replace(to_replace='7',value=7)
datos_comb['mes']=datos_comb['mes'].replace(to_replace='Agosto',value=8)
datos_comb['mes']=datos_comb['mes'].replace(to_replace='Septiembre',value=9)
datos_comb['mes']=datos_comb['mes'].replace(to_replace='Octubre',value=10)
datos_comb['mes']=datos_comb['mes'].replace(to_replace='Noviembre',value=11)
datos_comb['mes']=datos_comb['mes'].replace(to_replace='Diciembre',value=12)
datos_comb['mes']=datos_comb['mes'].replace(to_replace='12',value=12)
#Precios en año dado:
anho=int(input('Año a graficar:'))
datos_anho=datos_comb[datos_comb['periodo']==anho]
fechas_comb=pd.pivot_table(datos_anho,values='precio',index='mes',columns='producto',aggfunc=np.mean)
anho=str(anho)
fechas_comb.plot()
plt.title('Precio mensual de combustibles en Colombia '+anho,loc='left')
plt.title('cadecastro.com',loc='right')
gascor=datos_anho[datos_anho['producto']=='GASOLINA EXTRA']
municipio_gascor=pd.pivot_table(gascor,values='precio',index='mes',columns='municipio')
municipio_gascor=municipio_gascor.sort_values(by=municipio_gascor.index,ascending=True)