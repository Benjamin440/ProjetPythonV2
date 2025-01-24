import sys
import os
import getpass
import re
import SqlRequest
from User import User
import Crud

def authent(email, password):
    password = User.hash_password(None, password)
    res = SqlRequest.select_user(email)
    if password == res[0][7]:
        print("Vous êtes connecté")
        return True
    else:
        print("Mauvais nom d'utilisateur ou mot de passe")
        return False

def verify_role(email):
    res = SqlRequest.select_user(email)
    if res[0][8] == "UTILISATEUR":
        Crud.menu_utilisateur()
    elif res[0][8] == "ADMIN":
        Crud.menu_admin()
    else:
        Crud.menu_super_admin()