# -*- coding: utf-8 -*-
"""
ANÁLISIS CIFRAS VÍCTIMAS DELITOS COLOMBIA
Autor: Carlos Armando De Castro (cadecastro.com)
"""
import pandas as pd, matplotlib.pyplot as plt, numpy as np
#Importar de Datos Abiertos:
datos=pd.read_csv('https://www.datos.gov.co/api/views/sft7-9im5/rows.csv',usecols=['ANIO_HECHO','DEPARTAMENTO','MUNICIPIO','GRUPO_DELITO','DELITO','TOTAL_VICTIMAS'])
datos=datos.replace(to_replace={'BOGOTÁ, D. C.':'Bogotá, D.C.','Archipiélago de San Andrés, Providencia y Santa Catalina':'Archipiélago de San Andrés','Boyaca':'Boyacá','Quindío':'Quindio'})
datos['MUNICIPIO']=datos['MUNICIPIO'].str.title()
#Víctimas anuales:
anual=pd.pivot_table(datos,values='TOTAL_VICTIMAS',index='ANIO_HECHO',columns='GRUPO_DELITO',aggfunc=np.sum)
anual=anual.drop(index=[2055,2205])

#Lectura datos población departamental:
pob=pd.read_excel('https://www.dane.gov.co/files/censo2018/proyecciones-de-poblacion/Departamental/anexo-proyecciones-poblacion-departamental_Area2018-2050.xlsx',sheet_name=0,skiprows=11)
pob=pob[(pob['AÑO']==2021)&(pob['ÁREA GEOGRÁFICA']=='Total')].set_index('DPNOM').drop(columns=['DP','AÑO','ÁREA GEOGRÁFICA']).rename(columns={'Total':'Población 2021'})

#Lectura datos población municipal:
anho=2021
pob_mun=pd.read_excel('https://www.dane.gov.co/files/censo2018/proyecciones-de-poblacion/Municipal/anexo-proyecciones-poblacion-Municipal_Area_2018-2035.xlsx',sheet_name=0,skiprows=11)
pob_mun=pob_mun[(pob_mun['AÑO']==anho)&(pob_mun['ÁREA GEOGRÁFICA']=='Total')].set_index('MPIO').drop(columns=['DPMP',
                                                                                'DP','AÑO','ÁREA GEOGRÁFICA']).rename(columns={'Total':'Población 2021'})
pob_mun=pob_mun[pob_mun['Población '+str(anho)]>200000] #Sólo municipios con más de 200k habitantes.
pob_mun.index=pob_mun.index.str.title()

print('-------------------------------------------------------------')
print('          ANÁLISIS CIFRAS VÍCTIMAS DELITOS COLOMBIA          ')
print('       Autor: Carlos Armando De Castro (cadecastro.com)      ')
print('__________________________________________________________________')
print('       Homicidios dolosos en Colombia 2021:',np.format_float_positional(anual['HOMICIDIO DOLOSO'][2021],precision=0))
print('Promedio diario Homicidios dolosos en 2021:',np.format_float_positional(anual['HOMICIDIO DOLOSO'][2021]/365,precision=1))
print('__________________________________________________________________')

cdc=1
#Grupo de delitos en departamentos:
delitos=['HOMICIDIO DOLOSO','HURTO','SECUESTRO SIMPLE','EXTORSION']
deptos2021={}
for delito in delitos:
  deptos2021[delito]=pd.pivot_table(data=datos[(datos['GRUPO_DELITO']==delito)&(datos['ANIO_HECHO']==2021)],values='TOTAL_VICTIMAS',index='DEPARTAMENTO',aggfunc=np.sum)
  deptos2021[delito]=deptos2021[delito].join(pob) 
  deptos2021[delito]['Víctimas/100k']=deptos2021[delito]['TOTAL_VICTIMAS']/deptos2021[delito]['Población 2021']*100000
  deptos2021[delito]=deptos2021[delito].sort_values(by='Víctimas/100k',ascending=False)

  plt.figure(cdc,figsize=(12,5))
  plt.bar(deptos2021[delito].index,deptos2021[delito]['Víctimas/100k'],color='navy')
  plt.title('VÍCTIMAS DE '+delito+' POR CADA 100,000 HABITANTES EN 2021')
  plt.xticks(rotation=90)
  plt.grid(axis='y')
  plt.ylabel('Víctimas/100k habitantes')
  plt.xlabel('Fuente: https://www.datos.gov.co/api/views/sft7-9im5/rows.csv - Análisis: https://cadecastro.com')
  cdc+=1

#Gráficas delitos por año:

for delito in delitos:
  plt.figure(cdc,figsize=(10,5))
  plt.bar(anual.index,anual[delito],color='navy')
  plt.title('VÍCTIMAS DE '+delito+' EN COLOMBIA',loc='left')
  plt.title('cadecastro.com',loc='right')
  plt.xlabel('FUENTE: https://www.datos.gov.co/api/views/sft7-9im5/rows.csv')
  plt.grid(axis='y')
  plt.xticks(ticks=anual.index)
  cdc+=1

muns2021={}
for delito in delitos:
  muns2021[delito]=pd.pivot_table(data=datos[(datos['GRUPO_DELITO']==delito)&(datos['ANIO_HECHO']==2021)],values='TOTAL_VICTIMAS',index='MUNICIPIO',aggfunc=np.sum)
  muns2021[delito].rename(index={'Cartagena':'Cartagena De Indias'},inplace=True)
  muns2021[delito]=muns2021[delito].join(pob_mun).dropna()
  muns2021[delito]['Víctimas/100k']=muns2021[delito]['TOTAL_VICTIMAS']/muns2021[delito]['Población 2021']*100000
  muns2021[delito]=muns2021[delito].sort_values(by='Víctimas/100k',ascending=False)

  plt.figure(cdc,figsize=(12,5))
  plt.bar(muns2021[delito].index,muns2021[delito]['Víctimas/100k'],color='navy')
  plt.title('VÍCTIMAS DE '+delito+' POR CADA 100,000 HABITANTES EN 2021')
  plt.xticks(rotation=90)
  plt.grid(axis='y')
  plt.ylabel('Víctimas/100k habitantes')
  plt.xlabel('Fuente: https://www.datos.gov.co/api/views/sft7-9im5/rows.csv - Análisis: https://cadecastro.com')
  cdc+=1

anuales_dep={}
for delito in delitos:
  anuales_dep[delito]=pd.pivot_table(data=datos[(datos['GRUPO_DELITO']==delito)],values='TOTAL_VICTIMAS',index='ANIO_HECHO',columns='DEPARTAMENTO',aggfunc=np.sum)
  #anuales_dep[delito]=anuales_dep[delito].drop(index=[2055,2205])


anuales_mun={}
for delito in delitos:
  anuales_mun[delito]=pd.pivot_table(data=datos[(datos['GRUPO_DELITO']==delito)],values='TOTAL_VICTIMAS',index='ANIO_HECHO',columns='MUNICIPIO',aggfunc=np.sum)
  #anuales_mun[delito]=anuales_mun[delito].drop(index=[2055,2205])

municipio=str('Barranquilla')

for delito in delitos:
  plt.figure(cdc,figsize=(12,5))
  plt.bar(anuales_mun[delito].index,anuales_mun[delito][municipio],color='navy')
  plt.title('Víctimas de '+delito+' por año en '+municipio)
  plt.xticks(rotation=90)
  plt.grid(axis='y')
  plt.ylabel('Víctimas')
  plt.xlabel('Fuente: https://www.datos.gov.co/api/views/sft7-9im5/rows.csv - Análisis: https://cadecastro.com')
  cdc+=1

depto=str('Atlántico')

for delito in delitos:
  plt.figure(cdc,figsize=(12,5))
  plt.bar(anuales_dep[delito].index,anuales_dep[delito][depto],color='navy')
  plt.title('VÍCTIMAS DE '+delito+' POR AÑO - '+depto)
  plt.xticks(rotation=90)
  plt.grid(axis='y')
  plt.ylabel('Víctimas')
  plt.xlabel('Fuente: https://www.datos.gov.co/api/views/sft7-9im5/rows.csv - Análisis: https://cadecastro.com')
  cdc+=1
