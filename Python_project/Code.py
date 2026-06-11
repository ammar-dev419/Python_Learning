import json
try:
    with open("students.json", "r") as file:
        students = json.load(file)
except FileNotFoundError:
    print("Le fichier n'existe pas dans ce dossier.")
    students = []

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file)

def ajouter():
    new_student_name = input("Entrez le nom de l'etudiant: ")
    new_student_grade = float(input("Entrez la note de l'etudiant: "))
    if 0 <= new_student_grade <= 20:
        new_student = {"Nom": new_student_name, "Note": new_student_grade}
        students.append(new_student)
        save_students()
        print("L'eleve a ete ajoute avec succes")
    else:
        print("Error, Veuillez reessaye.")
    
def supprimer():
    student_name = input("Entrez le nombre de l'etudient: ")
    found = False
    for student in students:
        if student_name == student["Nom"]:
            students.remove(student)
            save_students()
            print("L'eleve a ete exclu avec succes.")
            found = True
            break
    if not found:
        print("L'etudiant n'existe pas.")

def afficher():
    for student in students:
        print("=====================")
        print(f"Nom: {student['Nom']}")
        print(f"Note: {student['Note']}")
        print("=====================")

def rechercher():
    search_student = input("Trouve un etudiant: ")
    found = False
    for student in students:
        if search_student == student["Nom"]:
            print(f"L'etudient a ete retrouve, son note est : {student['Note']}")
            found = True
            break
    if not found:
        print("L'etudient n'a pas retrouve")

def moyenne():
    if len(students) == 0:
        print("Aucun etudiant.")
        return
    total = 0
    for student in students:
       total += student["Note"]
    moyenne = total / len(students)
    print(f"La moyenne de classe est :{moyenne}")

def amendment():
    students_change = input("Entrez le nom de l'etudiant: ")
    found = False
    for student in students:
        if students_change == student['Nom']:
            found = True
            new_note = float(input("Entrez la nouvelle note: "))
            if new_note >= 0 and new_note <= 20:
                student['Note'] = new_note
                save_students()
                print("La note a ete modifie avec succes.")
            else:
                print("Error, Veuillez reessayer.")
            break
    if not found:
        print("L'etudiant n'exuste pas.")


while True:
    print("1. Ajouter")
    print("2. Supprimer")
    print("3. Rechercher")
    print("4. Afficher")
    print("5. Moyenne")
    print("6. Amendement")
    print("7. Quitter\n")
    command_list = str(input("Choisissez votre commande: "))

    if command_list == "1":
        ajouter()
    
    elif command_list == "2":
        supprimer()
    
    elif command_list == "3":
        rechercher()
    
    elif command_list == "4":
        afficher()
    
    elif command_list == "5":
        moyenne()

    elif command_list == "6":
        amendment()

    elif command_list == "7":
        break