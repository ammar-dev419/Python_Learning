import json
from student import Student
students = []

def load_students():
    global students
    try:
        with open("students.json", "r") as file:
            data = json.load(file)
            students = []
            for student in data:
                students.append(Student.from_dict(student))
    except (FileNotFoundError, json.JSONDecodeError):
        students = []

def save_students():
    with open("students.json", "w") as file:
        json.dump([student.to_dict() for student in students], file, indent=4)

def ajouter():
    try:
        new_student_name = input("Entrez le nom de l'etudiant: ")
        found = False
        for student in students:
            if new_student_name == student.name:
                found = True
                break
        if found:
            print("Cet etudiant existe deja.")
        else:
            new_student_grade = float(input("Entrez la note de l'etudiant: "))
            if 0 <= new_student_grade <= 20:
                new_student = Student(new_student_name,new_student_grade)
                students.append(new_student)
                save_students()
                print("L'eleve a ete ajoute avec succes")
            else:
                print("Error, Veuillez reessaye.")
    except ValueError:
        print("Erreur, Veuillez ressaye.")
    
def supprimer():
    student_name = input("Entrez le nom de l'etudient: ")
    found = False
    for student in students:
        if student_name == student.name:
            students.remove(student)
            save_students()
            print("L'eleve a ete exclu avec succes.")
            found = True
            break
    if not found:
        print("L'etudiant n'existe pas.")

def afficher():
    if not students:
        print("Aucun etudiant.")
        return
    for student in students:
        student.afficher()

def rechercher():
    search_student = input("Trouve un etudiant: ")
    found = False
    for student in students:
        if search_student == student.name:
            print(f"L'etudient a ete retrouve, son note est : {student.note}")
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
       total += student.note
    moyenne = total / len(students)
    print(f"La moyenne de classe est :{moyenne}")

def amendment():
    try:
        students_change = input("Entrez le nom de l'etudiant: ")
        found = False
        for student in students:
            if students_change == student.name:
                found = True
                new_note = float(input("Entrez la nouvelle note: "))
                if new_note >= 0 and new_note <= 20:
                    student.note = new_note
                    save_students()
                    print("La note a ete modifie avec succes.")
                else:
                    print("Erreur, Veuillez reessayer.")
                break
        if not found:
            print("L'etudiant n'exuste pas.")
    except ValueError:
        print("Erreur, Veuillez reesayer")

def statistiques():
    if len(students) == 0:
        print("Aucun etudiant.")
        return
    m_n = students[0].note
    p_n = students[0].note
    n_e = len(students)
    for student in students:
        if student.note >= m_n:
            m_n = student.note
            m_e = student.name

        if student.note <= p_n:
            p_n = student.note
            p_e = student.name
    total = 0
    for student in students:
        total += student.note
    moyenne = total / len(students)
    print(f"Nombre d'etudiant : {n_e}")
    print(f"Meilleure note : {m_e} ===> {m_n}")
    print(f"Pire note : {p_e} ===> {p_n}")
    print(f"Moyenne : {moyenne}")
