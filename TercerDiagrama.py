
from matplotlib import pyplot as plt

from PrimerDiagrama import df_pen_sales

#purchase Date y Delivery Date
#print(df_pen_sales["Delivery Date"])
#print(df_pen_sales["Purchase Date"])

tiempo_de_entrega = (df_pen_sales["Delivery Date"] - df_pen_sales["Purchase Date"]).dt.days
df_pen_sales["Tiempo de entrega"] = tiempo_de_entrega
tiempo_medio_de_entrega = df_pen_sales.groupby("Item")["Tiempo de entrega"].mean().sort_values()
plt.figure(figsize=(10, 5))
tiempo_medio_de_entrega.plot(kind="bar", color="pink")
plt.title("Tiempo medio de entrega de productos")
plt.xlabel("Tipo de producto")
plt.ylabel("Tiempo medio de entrega")
plt.xticks(rotation=45, ha='right')
plt.show()


print(tiempo_medio_de_entrega)