# -*- coding: utf-8 -*-
"""
ANÁLISIS SUICIDIOS COLOMBIA 2016-2019
Autor: Carlos Armando De Castro (cadecastro.com)
"""
import numpy as np, pandas as pd, matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None  # default='warn'
#Lectura datos suicidios:
df=pd.read_csv('https://www.datos.gov.co/api/views/f75u-mirk/rows.csv').replace(to_replace={'Archipiélago de San Andrés, Providencia y Santa Catalina':'Archipiélago de San Andrés','Quindío':'Quindio'})
df['Dia del hecho']=df['Dia del hecho'].str.capitalize()
df['Mes del hecho']=df['Mes del hecho'].str.capitalize()
#Lectura datos población:
pob=pd.read_excel('https://www.dane.gov.co/files/censo2018/proyecciones-de-poblacion/Departamental/anexo-proyecciones-poblacion-departamental_Area2018-2050.xlsx',sheet_name=0,skiprows=11)
pob=pob[(pob['AÑO']==2019)&(pob['ÁREA GEOGRÁFICA']=='Total')].set_index('DPNOM').drop(columns=['DP','AÑO','ÁREA GEOGRÁFICA']).rename(columns={'Total':'Población 2019'})

#Departamentos:
deptos=pd.pivot_table(data=df,values='ID',index='Departamento del hecho DANE',aggfunc=np.count_nonzero).rename(columns={'ID':'Suicidios'})
deptos=deptos.join(pob).dropna()
deptos['Per capita (%)']=deptos['Suicidios']/deptos['Población 2019']*100
deptos=deptos.sort_values(by='Per capita (%)',ascending=False)
del pob

#Edades y sexo:
edades=pd.pivot_table(data=df,values='ID',index='Grupo de edad de la victima',
                      columns='Sexo de la victima',aggfunc=np.count_nonzero)

#Días:
diasl=['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
dias=pd.pivot_table(data=df,values='ID',index='Dia del hecho',aggfunc=np.count_nonzero)
dias['Frecuencia (%)']=dias['ID']/dias['ID'].sum()*100
dias=dias.reindex(diasl)

#Meses:
mesesl=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
meses=pd.pivot_table(data=df,values='ID',index='Mes del hecho',aggfunc=np.count_nonzero)
meses['Frecuencia (%)']=meses['ID']/meses['ID'].sum()*100
meses=meses.reindex(mesesl)

#Sexo:
sexo=pd.pivot_table(data=df,values='ID',index='Sexo de la victima',aggfunc=np.count_nonzero)
sexo['Frecuencia (%)']=sexo['ID']/sexo['ID'].sum()*100
sexo=sexo.sort_values(by='Frecuencia (%)',ascending=False)

print('-----------------------------------------')
print('  ANÁLISIS SUICIDIOS COLOMBIA 2016-2019  ')
print('Carlos Armando De Castro (cadecastro.com)')
print('-----------------------------------------')
print(' ')
print(edades)
print(' ')
print('-----------------------------------------')
print(' ')
print(dias)
print(' ')
print('-----------------------------------------')
print(' ')
print(meses)
print(' ')
print('-----------------------------------------')
print(' ')
print(sexo)
print(' ')
print('-----------------------------------------')
print(' ')
print(deptos)
print(' ')
print('-----------------------------------------')

edades.plot.bar(figsize=(12,6),color=['navy','violet'])
plt.title('Suicidios en Colombia 2016-2019 por edad y género')
plt.title('cadecastro.com',loc='right',size=8)
plt.grid(axis='y')
plt.ylabel('Cantidad de suicidios')

plt.figure(2,figsize=(12,6))
plt.bar(dias.index,dias['Frecuencia (%)'],color='navy')
plt.title('Suicidios en Colombia 2016-2019 por día del hecho')
plt.title('cadecastro.com',loc='right',size=8)
plt.grid(axis='y')
plt.ylabel('Frecuencia (%)')

plt.figure(3,figsize=(12,6))
plt.bar(meses.index,meses['Frecuencia (%)'],color='navy')
plt.title('Suicidios en Colombia 2016-2019 por mes del hecho')
plt.title('cadecastro.com',loc='right',size=8)
plt.grid(axis='y')
plt.ylabel('Frecuencia (%)')

plt.figure(4,figsize=(6,6))
plt.pie(sexo['ID'],labels=sexo.index,colors=['navy','violet'])
plt.title('Suicidios en Colombia por género 2016-2019')
plt.xlabel('cadecastro.com',size=8)

plt.figure(5,figsize=(12,6))
plt.bar(deptos.index,deptos['Per capita (%)'],color='navy')
plt.title('Suicidios en Colombia 2016-2019 per cápita')
plt.title('cadecastro.com',loc='right',size=8)
plt.ylabel('Suicidios/Población (%)')
plt.xticks(rotation=90,size=10)
plt.grid(axis='y')
