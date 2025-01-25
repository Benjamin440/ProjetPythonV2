import SqlRequest
from User import User
import Crud

def authent(login, password):
    password = User.hash_password(None, password)
    res = SqlRequest.select_user(login)
    if res and password == res[0][7]:
        print("Vous êtes connecté")
        return True
    else:
        print("Mauvais nom d'utilisateur ou mot de passe")
        return False

def verify_role(login):
    res = SqlRequest.select_user(login) 
    if res[0][8] == "UTILISATEUR":
        Crud.menu_utilisateur()
    elif res[0][8] == "ADMIN":
        Crud.menu_admin()
    else:
        Crud.menu_super_admin()

def verify_ville(ville):
    villes_autorisees = {"PARIS", "RENNES", "STRASBOURG", "GRENOBLE", "NANTES"}
    if not ville:
        raise ValueError("La ville ne peut pas être vide")
    if ville.upper() not in villes_autorisees:
        raise ValueError("La ville doit être parmi les suivantes : PARIS, RENNES, STRASBOURG, GRENOBLE, NANTES")
    return ville.upper()

def afficher_user_ville(ville):
    try:
        ville = verify_ville(ville)
        res2 = SqlRequest.select_ville(ville)
        if not res2:
            print(f"Aucun utilisateur trouvé pour la ville {ville}.")
            return
        print(f"Liste des utilisateurs pour la ville {ville} :")
        for row in res2:
            print(row) 
    except ValueError as e:
        print(f"Erreur : {e}")
