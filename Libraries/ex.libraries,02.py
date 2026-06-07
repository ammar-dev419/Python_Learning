import pandas as pd
import os
file_path = os.path.join(os.path.dirname(__file__), "data.csv")
df = pd.read_csv(file_path)
print(df)

average_age = df['age'].mean()
print(f"Age moyen: {average_age}")

max_score = df['score'].max()
print(f"Meilleure note: {max_score}")

sorted_df = df.sort_values(by='score', ascending=False)
print(sorted_df)