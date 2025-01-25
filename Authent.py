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
    ville = res[0][3]
    if res[0][8] == "UTILISATEUR":
        Crud.menu_utilisateur()
    elif res[0][8] == "ADMIN":
        Crud.menu_admin(ville)
    else:
        Crud.menu_super_admin(ville)


