class Compte:
    def __init__(self, solde):
        self.solde = solde

    def deposer(self,montant):
        self.solde += montant

    def retirer(self,montant):
        if montant <= self.solde:
            self.solde -= montant
        else:
            print("Pas assez de solde!")

compte = Compte(100)
compte.deposer(50)
compte.retirer(30)
print(compte.solde)