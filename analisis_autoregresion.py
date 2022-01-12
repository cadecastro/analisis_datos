#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 08:21:38 2021
Carlos Armando De Castro Payares - cadecastro.com
"""
def analisis_arima(x):
    import numpy as np, pandas as pd
    from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
    import matplotlib.pyplot as plt
    from pandas.plotting import register_matplotlib_converters
    register_matplotlib_converters()
    import statsmodels
    import pmdarima as pm
    plot_acf(x)
    plot_pacf(x)
    #Modelo Autoarima:
    modelo1 = pm.auto_arima(x, start_p=1, start_q=1,
                      test='adf',       # use adftest to find optimal 'd'
                      max_p=3, max_q=3, # maximum p and q
                      m=1,              # frequency of series
                      d=None,           # let model determine 'd'
                      seasonal=False,   # No Seasonality
                      start_P=0, 
                      D=0, 
                      trace=True,
                      error_action='ignore',  
                      suppress_warnings=True, 
                      stepwise=True)

    print(modelo1.summary())
    modelo1.plot_diagnostics()
    #Predicción:
    n_periods=int(input('Períodos a predecir = '))
    fc, confint = modelo1.predict(n_periods=n_periods, return_conf_int=True)
    index_of_fc = np.arange(len(x), len(x)+n_periods)

    # make series for plotting purpose
    fc_series = pd.Series(fc, index=index_of_fc)
    lower_series = pd.Series(confint[:, 0], index=index_of_fc)
    upper_series = pd.Series(confint[:, 1], index=index_of_fc)

    # Plot
    plt.figure(4)
    plt.plot(np.arange(len(x)),x,'b')
    plt.plot(fc_series, color='red')
    plt.fill_between(lower_series.index, 
                 lower_series, 
                 upper_series, 
                 color='yellow', alpha=.75)

    plt.title("Predicción Auto ARIMA")
    plt.xlabel("Períodos - cadecastro.com")
    plt.grid(True,'both','both')
    #Modelo manual ARIMA:
    print('MODELO MANUAL ARIMA:')
    p=int(input('p = '))
    d=int(input('d = '))
    q=int(input('q = '))
    modelo2=statsmodels.tsa.arima.model.ARIMA(x, order=(p,d,q))
    resultados2= modelo2.fit()
    print(resultados2.summary())
    # Gráfica de errores residuales:
    residuales = pd.DataFrame(resultados2.resid)
    fig, ax = plt.subplots(1,2)
    residuales.plot(title="Residuales", ax=ax[0])
    residuales.plot(kind='kde', title='Densidad de probabilidad', ax=ax[1])
    #Ajuste y predicción:
    n=n_periods
    predic2=resultados2.predict(0,len(x)+n)
    indice1=range(0,len(x))
    indice2=range(0,len(x)+n+1)
    plt.figure(6)
    plt.plot(indice1,x,'b')
    plt.plot(indice2,predic2,'r')
    plt.title("Predicción ARIMA manual")
    plt.xlabel("Períodos - cadecastro.com")
    plt.grid(True,'both','both')
    