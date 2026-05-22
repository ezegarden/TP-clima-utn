
import pandas as pd

# Leer dataset climático
df = pd.read_csv("datos/temperaturas.csv")

# Calcular estadísticas básicas
promedio = df["temperatura"].mean()
maxima = df["temperatura"].max()
minima = df["temperatura"].min()

# Mostrar resultados
print("Temperatura promedio:", promedio)
print("Temperatura máxima:", maxima)
print("Temperatura mínima:", minima)
