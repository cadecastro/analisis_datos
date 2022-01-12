#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 18:46:53 2021
ANÁLISIS CIFRAS DELITOS 2020 A OCT-2021 COLOMBIA
Autor: Carlos Armando De Castro (cadecastro.com)
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Importar datos:
datos_delitos=pd.read_csv('/home/cdc/Documents/Datos/delitos_2020_2021.csv')
delitos=pd.pivot_table(datos_delitos,values='CANT',index='ARMAS_MEDIOS',columns='DELITO',aggfunc=np.sum)
delitos=delitos.sort_values(by='ARTÍCULO 103. HOMICIDIO',ascending=False)
armas=pd.pivot_table(datos_delitos,values='CANT',index='ARMAS_MEDIOS',aggfunc=np.sum)
armas=armas.sort_values(by='CANT',ascending=False)
#Gráfica armas:
armas.plot.bar(rot=5,color='blue')
plt.title('Delitos en Colombia todo 2020 y 2021 hasta octubre por tipo de arma')
plt.ylabel('Cantidad de víctimas')

plt.figure(2)
plt.bar(delitos.index,delitos['ARTÍCULO 103. HOMICIDIO'],color='red')
plt.ylabel('Cantidad de víctimas')
plt.title('Víctimas de homicidio en Colombia todo 2020 y 2021 hasta octubre por tipo de arma usada')

plt.figure(3)
plt.bar(delitos.index,delitos['ARTÍCULO 111. LESIONES PERSONALES'],color='blue')
plt.ylabel('Cantidad de víctimas')
plt.title('Víctimas lesiones personales en Colombia todo 2020 y 2021 hasta octubre por tipo de arma usada')

plt.figure(4)
plt.bar(delitos.index,delitos['ARTÍCULO 239. HURTO PERSONAS'],color='yellow')
plt.ylabel('Cantidad de víctimas')
plt.title('Víctimas hurto a personas en Colombia todo 2020 y 2021 hasta octubre por tipo de arma usada')