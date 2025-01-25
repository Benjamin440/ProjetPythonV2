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
    res2 = SqlRequest.select_ville(ville)
    if ville == "":
        raise ValueError("La ville ne peut pas être vide")
    elif ville != res2[0][3]:
        raise ValueError("La ville n'est pas valide")
    else:
        return ville