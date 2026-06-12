from student_manager import *

load_students()

while True:
    print("1. Ajouter")
    print("2. Supprimer")
    print("3. Rechercher")
    print("4. Afficher")
    print("5. Moyenne")
    print("6. Amendement")
    print("7. Statistiques")
    print("8. Quitter\n")
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
        statistiques()

    elif command_list == "8":
        break

    else:
        print("Commande invalide.")