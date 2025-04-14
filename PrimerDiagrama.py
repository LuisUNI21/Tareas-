import pandas as pd
import matplotlib.pyplot as plt

File_path = "./Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(File_path, sheet_name="Pen Sales")

# Agrupar por "Item" y calcular el costo promedio de envío, luego ordenar

df_avg_pen_costs = df_pen_sales.groupby("Item")["Shipping Cost"].mean().sort_values()
print(df_avg_pen_costs)

# Graficar los resultados

plt.figure(figsize=(10, 5))
df_avg_pen_costs.plot(kind="barh", color="purple")
plt.title("Costos de envío promedio por producto")
plt.xlabel("Costo medio de envío")
plt.ylabel("Producto")
plt.show()



