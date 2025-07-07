import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from matplotlib.backends.backend_pdf import PdfPages
import warnings
import os

warnings.filterwarnings("ignore") 

os.makedirs("graficos_predicciones", exist_ok=True)

df = pd.read_excel("Ventas hasta Mayo.xlsx")
df = df.drop(index=0).reset_index(drop=True)
df.columns = ['Componente', 'Oct 2024', 'Nov 2024', 'Dic 2024', 'Ene 2025', 'Feb 2025', 'Mar 2025', 'Abr 2025', 'May 2025']

meses_hist = df.columns[1:].tolist()
meses_pred = ['Jun 2025', 'Jul 2025', 'Ago 2025']

resultados = []

pdf_path = "Graficos_Predicciones_ARIMA.pdf"
with PdfPages(pdf_path) as pdf:
    for idx, row in df.iterrows():
        componente = row['Componente']
        ventas = row[1:].astype(float).values

        if np.count_nonzero(ventas) < 4:
            continue

        try:

            modelo = ARIMA(ventas, order=(1, 1, 1))
            modelo_entrenado = modelo.fit()

            pred = modelo_entrenado.forecast(steps=3)
            resultados.append([componente] + list(pred))

            ventas_totales = np.concatenate((ventas, pred))
            meses_totales = meses_hist + meses_pred

            plt.figure(figsize=(10, 5))
            plt.plot(meses_hist, ventas, marker='o', label='Histórico')
            plt.plot(meses_pred, pred, marker='o', linestyle='--', label='Predicción')

            for i, valor in enumerate(pred):
                plt.text(len(meses_hist) + i, valor + max(ventas) * 0.05, f"{valor:.1f}", ha='center', fontsize=9)

            plt.title(f"Ventas de {componente} (ARIMA)")
            plt.xlabel("Mes")
            plt.ylabel("Unidades")
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.legend()
            plt.tight_layout()

            pdf.savefig()
            plt.close()

        except Exception as e:
            print(f"❌ Error con {componente}: {e}")
            continue

df_resultados = pd.DataFrame(resultados, columns=['Componente'] + meses_pred)
df_resultados.to_excel("Predicciones_Ventas_ARIMA.xlsx", index=False)

print("✅ Predicciones con ARIMA completadas:")
print("- 'Predicciones_Ventas_ARIMA.xlsx'")
print(f"- '{pdf_path}' con gráficos.")
