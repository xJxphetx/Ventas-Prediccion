<h1 align="center">🤖 AG Electrónica – Asistente de Predicción de Ventas</h1>

<p align="center">
  <img src="https://img.shields.io/badge/modelos-ARIMA_&_LSTM-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/python-3.10+-green?style=flat-square" />
  <img src="https://img.shields.io/badge/license-MIT-brightgreen?style=flat-square" />
</p>

---

##  Sobre el Proyecto

Este proyecto compara dos enfoques para la predicción de ventas:

-  📊 **ARIMA**: Modelo estadístico clásico
-  🧠 **LSTM**: Red neuronal recurrente profunda

Ambos scripts procesan datos históricos de ventas y generan predicciones gráficas y exportables.

---

##  Estructura del Repositorio

```
ventas-prediccion/
├── src/
│   ├── arima.py                 # Modelo ARIMA
│   └── prediccion.py            # Modelo LSTM (TensorFlow)
├── resultados/
│   ├── Predicciones_*.xlsx      # Resultados en Excel
│   └── Graficos_*.pdf           # Gráficos generados
├── docs/
│   └── descripcion_modelos.md   # Explicación técnica
├── requirements.txt             # Librerías necesarias
├── LICENSE                      # MIT License
└── README.md                    # Este archivo
```

---

##  Cómo Ejecutar

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/ventas-prediccion.git
cd ventas-prediccion
```

2. Instala dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta un modelo:

```bash
# Para ARIMA:
python src/arima.py

# Para LSTM:
python src/prediccion.py
```

---

##  Tecnologías

- `pandas`, `numpy`, `matplotlib`
- `statsmodels` (ARIMA)
- `tensorflow` (LSTM)
- `openpyxl` para exportar resultados

---

##  Comparación

| Modelo | Tipo | Ventajas | Entrenamiento |
|--------|------|----------|---------------|
| ARIMA  | Estadístico | Rápido, interpretable | ❌ No |
| LSTM   | Deep Learning | Flexible, potente | ✅ Sí |

---

##  Licencia

Este repositorio está licenciado bajo la [MIT License](LICENSE).

---

## 🙌 Autor

Creado por **@xJxphetx** – Julio 2025