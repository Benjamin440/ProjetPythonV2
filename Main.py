import Crud
import Authent
import getpass
def main ():
    print("Bienvenue sur le programme d'authentification")
    print("1. Connexion")
    print("2. Quitter")
    choix = input("Que voulez-vous faire ? ")

    if choix == "1":
        login = input("Entrez votre login: ")
        password = getpass.getpass("Entrez votre mot de passe: ")
        if Authent.authent(login, password) == True:
            Authent.verify_role(login)
        else:
            main()
    elif choix == "2":
        print("Au revoir")
        exit()

main()