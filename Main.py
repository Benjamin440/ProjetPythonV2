import Crud
import Authent
def main ():
    print("Bienvenue sur le programme d'authentification")
    print("1. Connexion")
    print("3. Quitter")
    choix = input("Que voulez-vous faire ? ")

    if choix == "1":
        email = input("Entrez votre email: ")
        password = input("Entrez votre mot de passe: ")
        Authent.authent(email, password)
        if Authent.verify_role(email):
            Crud.menu()
        else:
            print("Vous n'avez pas les droits pour accéder à cette page")

    elif choix == "2":
        print("Au revoir")
        exit()