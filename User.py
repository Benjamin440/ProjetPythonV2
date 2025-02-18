import re
import secrets
import string
import hashlib
from datetime import datetime, timedelta

class User(object):

    def __init__ (self, mat_user, nom, prenom, ville, numero, role, password ):
        self._mat_user = mat_user
        self._nom = nom
        self._prenom = prenom
        self._ville = ville
        self._numero = numero
        self._role = role
        self._email = self.gen_email()
        self._login = self.gen_login()
        self.__password = self.hash_password(password)
        self.password_expiry = self.set_password_expiry()


### GESTION NOM ###
    def get_nom(self):
        return self._nom
    
    def set_nom(self, nouveau_nom):
        if nouveau_nom == "":
            raise ValueError("Le nom ne peut pas être vide")
        else:
            self._nom = nouveau_nom
            print("Le nom a été modifié")

### GESTION PRENOM ###   
    def get_prenom(self):
        return self._prenom
    
    def set_prenom(self, nouveau_prenom):
        if nouveau_prenom == "":
            raise ValueError("Le prénom ne peut pas être vide")
        else:
            self._prenom = nouveau_prenom
            print("Le prénom a été modifié")

### GESTION Matricule user ###
    def get_mat_user(self):
        return self._mat_user
    
    def set_mat_user(self, nouveau_mat_user):
        if nouveau_mat_user == "":
            raise ValueError("Le matricule ne peut pas être vide")
        else:
            self._mat_user = nouveau_mat_user
            print("Le matricule étudiant a été modifié")

### GESTION VILLE ###
    def get_ville(self):
        return self._ville  
    
    def set_ville(self, nouvelle_ville):
        liste_ville = ["PARIS", "RENNES","STRASBOURG", "GRENOBLE", "NANTES"]
        if nouvelle_ville == "":
            raise ValueError("La ville ne peut pas être vide")
        else:
            for i in liste_ville :
                if nouvelle_ville.upper() != i:
                    resultat = False
                else:
                    resultat = True
                    break
            if resultat == False:
                raise ValueError("La ville n'est pas dans la liste")
            else:
                self._ville = nouvelle_ville
                print("La ville a été modifié")

### GESTION NUMERO ###
    def get_numero(self):
        return self._numero

### GESTION EMAIL User ###
    def get_email(self):
        return self.__email
    
    def gen_email(self):
        self.__email = self._prenom[0].lower()+self._nom.replace(" ", "").lower()+"@americanhospital.fr"

    def set_email(self, nouveau_email):
            regex = r"^[a-z0-9._-]+@[a-z0-9._-]+\.[a-z]{2,6}$"
            if nouveau_email == "":
                ("L'email ne peut pas être vide")
            else:
                if not re.match(regex, nouveau_email):
                    raise ValueError("L'email n'est pas valide")
                else:
                    self._email = nouveau_email
                    print("L'email a été modifié")

### GESTION LOGIN User###
    def get_login(self):
            return self.__login

    def gen_login(self):
        self.__login = self._prenom[0].lower()+self._nom.replace(" ", "").lower()

    def set_login(self, nouveau_login):
            if nouveau_login == "":
                raise ValueError("Le login ne peut pas être vide")
            else:
                self._login = nouveau_login
                print("Le login a été modifié")

### GESTION PASSWORD ###
    def get_password(self):
            return self.__password
    
    def hash_password(self, password_hash):
        hashed_password = hashlib.sha256(password_hash.encode()).hexdigest()
        return hashed_password

    def gen_password(self):
        alphabet = string.ascii_letters + string.digits
        password_length = 14
        for _ in range(password_length):
            self.__password =self.__password+ ''.join(secrets.choice(alphabet))
        self.__password = self.hash_password(self.__password)

    def set_password(self, nouveau_password):
            regex = r"^(?=.[A-Za-z])(?=.\d)[A-Za-z\d]{10,}$"
            if nouveau_password == "":
                raise ValueError("Le mot de passe ne peut pas être vide")
            elif re.search(regex, nouveau_password):
                self.__password = nouveau_password
            else : 
                raise ValueError("Le mot de passe n'est pas valide")
            
    def set_password_expiry(self, days_valid=90):
        return datetime.now() + timedelta(days=days_valid)
            
### GESTION DU ROLE ###
    def get_role(self):
        return self._role  
    
    def set_role(self, nouvelle_role):
        liste_role = ["UTILISATEUR", "ADMIN","SUPERADMIN"]
        if nouvelle_role == "":
            raise ValueError("La role ne peut pas être vide")
        else:
            for i in liste_role :
                if nouvelle_role.upper() != i:
                    resultat = False
                else:
                    resultat = True
                    break
            if resultat == False:
                raise ValueError("La role n'est pas dans la liste")
            else:
                self._role = nouvelle_role
                print("La role a été modifié")

### AFFICHAGE user ###
    def afficher(self):
        print("-----------------------------")
        print("Informations de l'utilisateur :")
        print("Nom :" ,self.get_nom()) 
        print("Prenom :", self.get_prenom())
        print("Matricule de l'utilisateur :", self.get_mat_user())
        print("Ville :", self.get_ville())
        print("Numéro de téléphone :", self.get_numero())
        print("Role :", self.get_role())
        print("-----------------------------")

### AFFICHAGE USER ###
    def afficher_user(self):
        self.afficher()
        print("Email :", self.get_email())
        print("Login :", self.get_login())
        print("Password :", self.get_password())
        print("-----------------------------")


### CREATION DE LA CLASSE PHospitalier ###
class PHospitalier (User):
    def __init__ (self, nom, prenom, ville, numero, role, service, password, mat_user ):
            User.__init__(self, nom, prenom, ville, numero, role, password, mat_user)
            self._service = service

### GESTION SERVICE ###
    def get_service(self):
        return self._service

    def set_service(self, nouveau_service):
        liste_service = ["CARDIOLOGIE", "PNEUMOLOGIE","NEUROLOGIE", "REANIMATION", "ANESTHESIE", "URGENCE"]
        if nouveau_service == "":
            raise ValueError("La service ne peut pas être vide")
        else:
            for i in liste_service :
                if nouveau_service.upper() != i:
                    resultat = False
                else:
                    resultat = True
                    break
            if resultat == False:
                raise ValueError("La service n'est pas dans la liste")
            else:
                self._service = nouveau_service
                print("La service a été modifié")
    

### CREATION DE LA CLASSE Patient ###
class Patient (User):
    def __init__(self, nom, prenom, ville, numero, role, s_social, password, mat_user ):
            User.__init__(self, nom, prenom, ville, numero, role, password, mat_user)
            self._S_Social = s_social

### GESTION Sécurité Social ###
    def get_s_social(self):
        return self._S_Social

    def set_social(self, nouveau_s_social):
        if nouveau_s_social == "":
            raise ValueError("Le service ne peut pas être vide")
        else:
            self._Service = nouveau_s_social
            print("Le service a été modifié")



# ## Test de la classe User ##
# user1 = User("LE BERRE", "Benjamin","PARIS","0626738933","UTILISATEUR","ESGI"," ")
# user1.afficher_user()
