import pandas as pd
import os
class FileLoader:
    def __init__(self, filename):
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.data = []
    
    def load(self):
        df = pd.read_csv(self.filename)
        self.data = df
        return df

    def show(self):
        print(self.data)

class Analyser:
    def __init__(self, df):
        self.df = df

    def average_age(self):
        return self.df['age'].mean()

    def max_score(self):
        return self.df['score'].max()

    def min_score(self):
        return self.df['age'].min()

    def students_per_age(self):
        return self.df['age'].value_counts()

    def sort_by_score(self, ascending=False):
        return self.df.sort_values(by='score', ascending=ascending)

if __name__ == "__main__":
    loader = FileLoader("data.csv")
    df = loader.load()
    loader.show()
    analyser = Analyser(df)
    print("\nAge moyen:", analyser.average_age())
    print("Meilleure note:", analyser.max_score())
    print("Pire note:", analyser.min_score())
    print("\nNombre d'eleves par groupe d'age:")
    print(analyser.students_per_age())
    print("\nLes eleves sont tries par niveau scolaire.")
    print(analyser.sort_by_score())