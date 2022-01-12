#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 17:39:59 2021
ANÁLISIS CIFRAS HOMICIDIOS COLOMBIA DESDE 2010
Autor: Carlos Armando De Castro (cadecastro.com)
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Importar datos de Datos Abiertos Colombia:
columnas=['DEPARTAMENTO','FECHA HECHO','ARMAS MEDIOS','GENERO','DESCRIPCIÓN CONDUCTA','CANTIDAD']
homi=pd.read_csv('https://www.datos.gov.co/api/views/ha6j-pa2r/rows.csv',usecols=columnas)

#Separado por tipo de homicidio:
intencional=homi[homi['DESCRIPCIÓN CONDUCTA']=='HOMICIDIO']
intencional['FECHA HECHO']=pd.to_datetime(intencional['FECHA HECHO'],dayfirst=True)
fechas_int=pd.pivot_table(intencional,values='CANTIDAD',index='FECHA HECHO',columns='ARMAS MEDIOS',aggfunc=np.sum)
intencional['Año']=pd.DatetimeIndex(intencional['FECHA HECHO']).year
anho_int=pd.pivot_table(intencional,values='CANTIDAD',index='Año',columns='ARMAS MEDIOS',aggfunc=np.sum)
accidental=homi[homi['DESCRIPCIÓN CONDUCTA']=='HOMICIDIO CULPOSO ( EN ACCIDENTE DE TRÁNSITO)']
#Muertes  intencionales por medio:
intencional_medios=intencional.groupby(['ARMAS MEDIOS'])[['CANTIDAD']].sum()
intencional_medios=intencional_medios.sort_values(by=['CANTIDAD'],ascending=False)
print('ANÁLISIS DE HOMICIDIOS Y ACCIDENTES DE TRÁNSITO COLOMBIA DESDE 2010')
print('Homicidios intencionales:')
print(intencional_medios)
#Muertes  accidentales por medio:
accidental_medios=accidental.groupby(['ARMAS MEDIOS'])[['CANTIDAD']].sum()
accidental_medios=accidental_medios.sort_values(by=['CANTIDAD'],ascending=False)
print('Homicidios en accidentes de tránsito:')
print(accidental_medios)

#Género de homicidios:
sexo=pd.pivot_table(homi,values='CANTIDAD',index='GENERO',columns='DESCRIPCIÓN CONDUCTA',aggfunc=np.sum)
sexo=sexo.sort_values(by=['HOMICIDIO'],ascending=False)
#Muertes  accidentales por departamento:
accidental_dep=accidental.groupby(['DEPARTAMENTO'])[['CANTIDAD']].sum()
accidental_dep=accidental_dep.sort_values(by=['CANTIDAD'],ascending=False)
print('Hom. accidentes tránsito por departamento:')
print(accidental_dep)
#Muertes  intencionales por departamento:
intencional_dep=intencional.groupby(['DEPARTAMENTO'])[['CANTIDAD']].sum()
intencional_dep=intencional_dep.sort_values(by=['CANTIDAD'],ascending=False)
print('Homicidios intencionales por departamento:')
print(intencional_dep)

intencional_medios[:5].plot.bar(color='red')
plt.title('Homicidios por tipo de arma usada',loc='left')
plt.title('cadecastro.com',loc='right')

accidental_medios.plot.bar(color=['blue'])
plt.title('MUERTES ACC. DE TRÁNSITO DESDE 2010',loc='left')
plt.title('cadecastro.com',loc='right')

sexo.plot.bar(y=['HOMICIDIO','HOMICIDIO CULPOSO ( EN ACCIDENTE DE TRÁNSITO)'],color=['red','yellow'],rot=15)

plt.figure(4,figsize=(12,6))
plt.bar(anho_int.index,anho_int['ARMA DE FUEGO'],color='blue')
plt.title('Homicidios anuales por arma de fuego en Colombia')
plt.title('cadecastro.com',loc='right')

plt.figure(5,figsize=(12,6))
plt.bar(anho_int.index,anho_int['ARMA BLANCA / CORTOPUNZANTE'],color='blue')
plt.title('Homicidios anuales por arma blanca en Colombia')
plt.title('cadecastro.com',loc='right')

plt.figure(6,figsize=(12,6))
plt.bar(fechas_int.index,fechas_int['ARMA DE FUEGO'],color='blue')
plt.plot(fechas_int.index,fechas_int['ARMA DE FUEGO'].rolling(window=30).mean(),'r')
plt.title('Homicidios diarios por arma de fuego en Colombia')
plt.legend(['Media 30 días','Dato'])
plt.title('cadecastro.com',loc='right')

plt.figure(7,figsize=(12,6))
plt.bar(fechas_int.index,fechas_int['ARMA BLANCA / CORTOPUNZANTE'],color='blue')
plt.plot(fechas_int.index,fechas_int['ARMA BLANCA / CORTOPUNZANTE'].rolling(window=30).mean(),'r')
plt.legend(['Media 30 días','Dato'])
plt.title('cadecastro.com',loc='right')
plt.title('Homicidios diarios por arma blanca en Colombia')