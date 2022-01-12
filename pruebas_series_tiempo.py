#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 21:37:51 2021
Carlos Armando De Castro- cadecastro.com
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
    from statsmodels.tsa.seasonal import seasonal_decompose
    periodo=int(input('Período = '))
    desc_estacional=seasonal_decompose(X, model='additive', filt=None, period=periodo, two_sided=True, extrapolate_trend=0)
    desc_estacional.plot()
    return desc_estacional

def transformada_fourier(x):
    import numpy as np
    import matplotlib.pyplot as plt
    sr=float(input('Tasa de muestreo = '))
    X = np.fft.fft(x)
    N = len(X)
    n = np.arange(N)
    T = N/sr
    freq = n/T 
    plt.stem(freq,np.abs(X),'b',markerfmt=" ", basefmt="-b")
    plt.xlabel('Frecuencia')
    plt.ylabel('Amplitud FFT')
    
def prueba_autocorrelacion(x):
    import numpy as np, pandas as pd
    from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
    import matplotlib.pyplot as plt
    plot_acf(x)
    plt.title('Serie original',loc='right')
    plot_acf(x.diff().dropna())
    plt.title('Serie primera diferencia',loc='right')
    plot_acf(x.diff().diff().dropna())
    plt.title('Serie segunda diferencia',loc='right')