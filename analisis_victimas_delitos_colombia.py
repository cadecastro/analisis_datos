#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 11:19:27 2022
ANÁLISIS CIFRAS VÍCTIMAS DELITOS COLOMBIA
Autor: Carlos Armando De Castro (cadecastro.com)
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Importar de Datos Abiertos:
datos=pd.read_csv('https://www.datos.gov.co/api/views/sft7-9im5/rows.csv',usecols=['ANIO_HECHO','DEPARTAMENTO','GRUPO_DELITO','TOTAL_VICTIMAS'])
#Víctimas anuales:
anual=pd.pivot_table(datos,values='TOTAL_VICTIMAS',index='ANIO_HECHO',columns='GRUPO_DELITO',aggfunc=np.sum)
anual=anual.drop(index=[2055,2205])
#Gráfica homicidio doloso:
plt.figure(1,figsize=(12,6))
plt.bar(anual.index,anual['HOMICIDIO DOLOSO'],color='red')
plt.title('VÍCTIMAS DE HOMICIDIOS DOLOSOS EN COLOMBIA',loc='left')
plt.title('cadecastro.com',loc='right')
#Gráfica hurto:
plt.figure(2,figsize=(12,6))
plt.bar(anual.index,anual['HURTO'],color='red')
plt.title('VÍCTIMAS DE HURTO EN COLOMBIA',loc='left')
plt.title('cadecastro.com',loc='right')
#Gráfica secuestro simple:
plt.figure(3,figsize=(12,6))
plt.bar(anual.index,anual['SECUESTRO SIMPLE'],color='red')
plt.title('VÍCTIMAS DE SECUESTRO SIMPLE EN COLOMBIA',loc='left')
plt.title('cadecastro.com',loc='right')
#Gráfica secuestro extorsivo:
plt.figure(4,figsize=(12,6))
plt.bar(anual.index,anual['VIOLENCIA INTRAFAMILIAR'],color='red')
plt.title('VÍCTIMAS DE VIOLENCIA INTRAFAMILIAR EN COLOMBIA',loc='left')
plt.title('cadecastro.com',loc='right')
#Gráfica amenazas:
plt.figure(5,figsize=(12,6))
plt.bar(anual.index,anual['AMENAZAS'],color='red')
plt.title('VÍCTIMAS DE AMENAZAS EN COLOMBIA',loc='left')
plt.title('cadecastro.com',loc='right')
#Gráfica extorsión:
plt.figure(6,figsize=(12,6))
plt.bar(anual.index,anual['EXTORSION'],color='red')
plt.title('VÍCTIMAS DE EXTORSION EN COLOMBIA',loc='left')
plt.title('cadecastro.com',loc='right')