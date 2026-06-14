class Student:
    def __init__(self, name, note):
        self.name = name
        self.note = note 

    def to_dict(self):
        return {
            "Nom": self.name, 
            "Note": self.note
        }
    
    @staticmethod
    def from_dict(data):
        return Student(data["Nom"], data["Note"])
    
    def afficher(self):
        print("=====================")
        print(f"Nom: {self.name}")
        print(f"Note: {self.note}")
        print("=====================")