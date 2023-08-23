import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

name = 'TSLA'
name = 'MELI'
name = 'AMZN'
accName = yf.Ticker(name)
m1 = 10
m2 = 40

# get historical market data
hist = accName.history(period="5y")
histClose = hist['Close']

mvs1 = histClose.rolling(window=m1).mean()
mvs2 = histClose.rolling(window=m2).mean()

# Crear un DataFrame con las columnas deseadas
data = pd.DataFrame(
    {name: histClose, 'MVS1': mvs1, 'MVS2': mvs2})


def signal(data):
    compra = []
    venta = []
    condicion = 0

    for dia in range(len(data)):
        if data['MVS1'][dia] > data['MVS2'][dia]:
            if condicion != 1:
                compra.append(data[name][dia])
                venta.append(np.nan)
                condicion = 1
            else:
                compra.append(np.nan)
                venta.append(np.nan)
        elif data['MVS1'][dia] < data['MVS2'][dia]:
            if condicion != -1:
                venta.append(data[name][dia])
                compra.append(np.nan)
                condicion = -1
            else:
                compra.append(np.nan)
                venta.append(np.nan)
        else:
            compra.append(np.nan)
            venta.append(np.nan)
            condicion = 0

    return (compra, venta)

senales = signal(data)
data['Compra'] = senales[0]
data['Venta'] = senales[1]

plt.figure(figsize=(10,5))
plt.plot(histClose, label=name)
plt.plot(mvs1, label= f'MVS{m1}')
plt.plot(mvs2, label= f'MVS{m2}')
plt.scatter(data.index, data['Compra'], label = 'Precio de compra', marker='^', color='green')
plt.scatter(data.index, data['Venta'], label = 'Precio de venta', marker='v', color='red')
plt.legend(loc='upper center')
plt.show()

last_non_nan_index = data[data['Compra'].notna()].index[-1]
last_non_nan_row = data.loc[last_non_nan_index]

print("Última fila con Compra no NaN:")
print(last_non_nan_row)
