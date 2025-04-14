import pandas as pd

File_path = "./Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(File_path, sheet_name="Pen Sales")

print(df_pen_sales.dtypes)



