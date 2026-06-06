
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos/dataset.csv")

# Convertimos la columna de fecha a datetime para poder agrupar por mes correctamente
df["sales_date"] = pd.to_datetime(df["sales_date"])

# Indicadores globales
# Calculamos métricas de resumen para interpretar el desempeño general de ventas
ventas_totales = df["sales_amount"].sum()
producto_mas_vendido = df.loc[df["sales_amount"].idxmax(), "sales_date"]

print("=== INDICADORES DE VENTAS ===")
print(f"Ventas totales:         ${ventas_totales:,.2f}")
print(f"Venta máxima el:        {producto_mas_vendido.date()}")
print(f"Venta mínima:           ${df['sales_amount'].min():,.2f}")
print(f"Promedio diario:        ${df['sales_amount'].mean():,.2f}")

# Ventas por mes
# Agrupamos por mes para detectar tendencias a lo largo del período
df["mes"] = df["sales_date"].dt.to_period("M")
ventas_por_mes = df.groupby("mes")["sales_amount"].sum().reset_index()
ventas_por_mes["mes"] = ventas_por_mes["mes"].astype(str)

print("\n=== VENTAS POR MES ===")
print(ventas_por_mes.to_string(index=False))

# Guardamos el resumen mensual en /resultados
ventas_por_mes.to_csv("resultados/resumen_ventas_por_mes.csv", index=False)

# Gráfico de evolución de ventas
# Visualizamos la evolución mensual para identificar picos y caídas
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(ventas_por_mes["mes"], ventas_por_mes["sales_amount"], marker="o", linewidth=2)
ax.set_title("Evolución Mensual de Ventas")
ax.set_xlabel("Mes")
ax.set_ylabel("Monto total ($)")
ax.tick_params(axis="x", rotation=45)
ax.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()

# Guardamos el gráfico en /resultados
plt.savefig("resultados/grafico_ventas_mensuales.png", dpi=150)
plt.show()
print("Gráfico guardado en resultados/grafico_ventas_mensuales.png")
