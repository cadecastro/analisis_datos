#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:05:12 2021
Pruebas para series de tiempo
"""
def prueba_dickey_fuller(X):
    from statsmodels.tsa.stattools import adfuller
    result=adfuller(X)
    print('Estadística ADF = %f' % result[0])
    print('p-value = %f' % result[1])
    print('Valores críticos:')
    for key, value in result[4].items():
        print('\t%s: %.3f' % (key, value))
    if result[1]>0.05:
       print('Datos no son estacionarios.')
    else:
       print('Datos son estacionarios.')
       
def prueba_estacionalidad(X):
    import statsmodels as st
    periodo=input('Período = ')
    desc_estacional=st.tsa.seasonal.seasonal_decompose(X, model='additive', filt=None, period=periodo, two_sided=True, extrapolate_trend=0)
    desc_estacional.plot()
    return desc_estacional