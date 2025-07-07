# 🧠 Descripción Técnica – ARIMA vs LSTM

Este documento explica la lógica y el propósito de los dos modelos aplicados.

---

## 📈 ARIMA (AutoRegressive Integrated Moving Average)

- Modelo clásico de series temporales.
- Basado en tendencias, estacionalidades y ruido.
- Requiere ajustar parámetros (p, d, q) mediante AIC/BIC.
- Ideal para patrones estables en el tiempo.

---

## 🤖 LSTM (Long Short-Term Memory)

- Red neuronal especializada en secuencias.
- Puede capturar no linealidades y relaciones complejas.
- Requiere entrenamiento con múltiples épocas.
- Usa TensorFlow/Keras y produce resultados más flexibles.

---

## 🧪 Dataset esperado

Ambos modelos trabajan con una columna `ventas` con datos diarios, semanales o mensuales.