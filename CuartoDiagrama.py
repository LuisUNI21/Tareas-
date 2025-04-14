import pandas as pd
import matplotlib.pyplot as plt

file_path = "./Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(file_path, sheet_name="Pen Sales")

reviews = df_pen_sales["Review"]

positive_words = ["love", "great", "good", "amazing", "excellent", "best" ]
negative_words = ["bad", "poor", "dislike", "terrible", "worst", "disappointed", "unfortunately"]

positive_review_count = reviews.str.contains("|".join(positive_words), case = False, na = False).sum()
negative_review_count = reviews.str.contains("|".join(negative_words), case = False, na = False).sum()

print("Cantidad de Reviews Positivos: " +str(positive_review_count))
print("Cantidad de Reviews Negativos: " +str(negative_review_count))

plt.figure(figsize = (6, 6))
plt.pie(x=[positive_review_count, negative_review_count], labels=["Review Positivo", "Review Negativo"], autopct="%1.1f%%", colors=["green", "red"], startangle=140)
plt.title("Opiniones")
plt.show()
