#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANÁLISIS CIFRAS VÍCTIMAS DELITOS COLOMBIA
Autor: Carlos Armando De Castro (cadecastro.com)
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Importar de Datos Abiertos:
datos=pd.read_csv('https://www.datos.gov.co/api/views/sft7-9im5/rows.csv',usecols=['ANIO_HECHO','DEPARTAMENTO','GRUPO_DELITO','DELITO','TOTAL_VICTIMAS'])
#Víctimas anuales:
anual=pd.pivot_table(datos,values='TOTAL_VICTIMAS',index='ANIO_HECHO',columns='GRUPO_DELITO',aggfunc=np.sum)
anual=anual.drop(index=[2055,2205])

print('-------------------------------------------------------------')
print('          ANÁLISIS CIFRAS VÍCTIMAS DELITOS COLOMBIA          ')
print('       Autor: Carlos Armando De Castro (cadecastro.com)      ')
print('__________________________________________________________________')
print('       Homicidios dolosos en Colombia 2021:',np.format_float_positional(anual['HOMICIDIO DOLOSO'][2021],precision=0))
print('Promedio diario Homicidios dolosos en 2021:',np.format_float_positional(anual['HOMICIDIO DOLOSO'][2021]/365,precision=1))
print('__________________________________________________________________')

#Gráficas delitos:
delitos=['HOMICIDIO DOLOSO','HURTO','SECUESTRO SIMPLE','VIOLENCIA INTRAFAMILIAR','EXTORSION']
cdc=1
for delito in delitos:
  plt.figure(cdc,figsize=(10,5))
  plt.bar(anual.index,anual[delito],color='navy')
  plt.title('VÍCTIMAS DE '+delito+' EN COLOMBIA',loc='left')
  plt.title('cadecastro.com',loc='right')
  plt.xlabel('FUENTE: https://www.datos.gov.co/api/views/sft7-9im5/rows.csv')
  plt.grid(axis='y')
  plt.xticks(ticks=anual.index)
  cdc+=1
#Grupo de delitos:
grupo=str('HOMICIDIO DOLOSO')
hom2=pd.pivot_table(data=datos[datos['GRUPO_DELITO']==grupo],values='TOTAL_VICTIMAS',index='ANIO_HECHO',columns='DELITO',aggfunc=np.sum)
print(hom2.columns)

for delito in hom2.columns:
  plt.figure(cdc,figsize=(15,5))
  plt.bar(hom2.index,hom2[delito],color='navy')
  plt.title(delito,loc='left')
  plt.title('cadecastro.com',loc='right')
  plt.xlabel('FUENTE: https://www.datos.gov.co/api/views/sft7-9im5/rows.csv')
  plt.grid(axis='y')
  plt.xticks(ticks=anual.index)
  cdc+=1
