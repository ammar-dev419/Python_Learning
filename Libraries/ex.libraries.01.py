import csv
import os
class FileLoader:
    def __init__(self, filename):
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.data = []
    
    def load(self):
        with open(self.filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.data.append(row)
        return self.data

    def show(self):
        for row in self.data:
            print(row)

if __name__ == "__main__":
    loader = FileLoader("data.csv")
    loader.load()
    loader.show()