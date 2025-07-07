# 📊 Predicción de Ventas con ARIMA y LSTM

Este proyecto compara dos métodos para la predicción de series temporales de ventas:

- `ARIMA` (modelo estadístico tradicional)
- `LSTM` (modelo de red neuronal recurrente)

Ambos scripts utilizan datos históricos de ventas y generan predicciones para períodos futuros, incluyendo visualización y exportación de resultados a Excel y PDF.

---

## 📁 Estructura del proyecto

```bash
ventas-prediccion/
├── src/
│   ├── arima.py                   # Predicción usando modelo ARIMA
│   └── prediccion.py              # Predicción usando red neuronal LSTM
├── resultados/
│   ├── Predicciones_Ventas_ARIMA.xlsx
│   ├── Predicciones_Ventas_Futuras.xlsx
│   ├── Graficos_Predicciones_ARIMA.pdf
│   └── Graficos_Predicciones.pdf
├── docs/
│   └── descripcion_modelos.md     # Explicación técnica de los modelos
└── README.md
```

---

## 🚀 ¿Cómo ejecutar?

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/ventas-prediccion.git
cd ventas-prediccion
```

### 2. Instalar dependencias

```bash
pip install pandas numpy matplotlib tensorflow statsmodels openpyxl
```

### 3. Ejecutar scripts

#### Modelo ARIMA:

```bash
python src/arima.py
```

#### Modelo LSTM (deep learning):

```bash
python src/prediccion.py
```

---

## 📦 Salidas

- `resultados/Predicciones_*.xlsx` → Predicciones futuras
- `resultados/Graficos_*.pdf` → Visualizaciones de desempeño

---

## 🧠 Comparación breve

| Modelo | Tipo          | Ventajas                          | Requiere entrenamiento |
|--------|---------------|-----------------------------------|------------------------|
| ARIMA  | Estadístico   | Rápido, interpretabilidad alta    | ❌ No                  |
| LSTM   | Deep Learning | Aprende patrones complejos        | ✅ Sí                  |

---

## 👤 Autor

Desarrollado por [Tu Nombre]  
Última actualización: Julio 2025