import Crud
import Authent
def main ():
    print("Bienvenue sur le programme d'authentification")
    print("1. Connexion")
    print("2. Quitter")
    choix = input("Que voulez-vous faire ? ")

    if choix == "1":
        email = input("Entrez votre email: ")
        password = input("Entrez votre mot de passe: ")
        Authent.authent(email, password)
        Authent.verify_role(email)
    elif choix == "2":
        print("Au revoir")
        exit()

main()