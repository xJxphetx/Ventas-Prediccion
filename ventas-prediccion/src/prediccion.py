import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from matplotlib.backends.backend_pdf import PdfPages
import os

# Crear carpeta si se desea guardar imágenes también
os.makedirs("graficos_predicciones", exist_ok=True)

# Cargar y limpiar Excel
df = pd.read_excel("Ventas hasta Mayo.xlsx")
df = df.drop(index=0).reset_index(drop=True)
df.columns = ['Componente', 'Oct 2024', 'Nov 2024', 'Dic 2024', 'Ene 2025', 'Feb 2025', 'Mar 2025', 'Abr 2025', 'May 2025']

meses_hist = df.columns[1:].tolist()
meses_pred = ['Jun 2025', 'Jul 2025', 'Ago 2025']

resultados = []

def crear_secuencias(datos, pasos=3):
    X, y = [], []
    for i in range(len(datos) - pasos):
        X.append(datos[i:i+pasos])
        y.append(datos[i+pasos])
    return np.array(X), np.array(y)

# PDF para guardar gráficos
pdf_path = "Graficos_Predicciones.pdf"
with PdfPages(pdf_path) as pdf:
    for idx, row in df.iterrows():
        componente = row['Componente']
        ventas = row[1:].astype(float).values

        if np.count_nonzero(ventas) < 4:
            continue

        scaler = MinMaxScaler()
        ventas_normalizadas = scaler.fit_transform(ventas.reshape(-1, 1))

        X, y = crear_secuencias(ventas_normalizadas, pasos=3)
        if X.shape[0] == 0:
            continue
        X = np.reshape(X, (X.shape[0], X.shape[1], 1))

        modelo = Sequential()
        modelo.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)))
        modelo.add(Dropout(0.2))
        modelo.add(LSTM(50))
        modelo.add(Dropout(0.2))
        modelo.add(Dense(1))
        modelo.compile(optimizer='adam', loss='mean_squared_error')

        try:
            modelo.fit(X, y, epochs=100, batch_size=4, verbose=0)
        except:
            continue

        predicciones = []
        entrada = ventas_normalizadas[-3:]
        for _ in range(3):
            entrada_reshaped = np.reshape(entrada, (1, 3, 1))
            pred = modelo.predict(entrada_reshaped, verbose=0)
            predicciones.append(pred[0][0])
            entrada = np.append(entrada[1:], pred, axis=0)

        predicciones_futuras = scaler.inverse_transform(np.array(predicciones).reshape(-1, 1)).flatten()
        resultados.append([componente] + list(predicciones_futuras))

        # Crear gráfico con etiquetas
        ventas_totales = np.concatenate((ventas, predicciones_futuras))
        meses_totales = meses_hist + meses_pred

        plt.figure(figsize=(10, 5))
        plt.plot(meses_hist, ventas, marker='o', label='Histórico')
        plt.plot(meses_pred, predicciones_futuras, marker='o', linestyle='--', label='Predicción')

        # Agregar etiquetas a puntos de predicción
        for i, valor in enumerate(predicciones_futuras):
            plt.text(len(meses_hist) + i, valor + max(ventas) * 0.05, f"{valor:.1f}", ha='center', fontsize=9)

        plt.title(f"Ventas de {componente}")
        plt.xlabel("Mes")
        plt.ylabel("Unidades")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        pdf.savefig()
        plt.close()

# Guardar predicciones en Excel
df_resultados = pd.DataFrame(resultados, columns=['Componente'] + meses_pred)
df_resultados.to_excel("Predicciones_Ventas_Futuras.xlsx", index=False)

print("✅ Todo generado con éxito:")
print("- 'Predicciones_Ventas_Futuras.xlsx'")
print(f"- '{pdf_path}' con etiquetas de valores en los gráficos.")
