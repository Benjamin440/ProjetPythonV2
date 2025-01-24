from User import User as U
from User import PHospitalier as PH
from User import Patient as P
import SqlRequest
import sqlite3

### Constantes ###
AJOUT_USER = "Ajout d'un utilisateur "
AJOUT_OK = "Utilisateur ajouté"
NOM_USER = "Entrez le nom : "
PRENOM_USER = "Entrez le prénom : "
VILLE_USER = "Entrez la ville : "
NUMERO_USER = "Entrez le numéro : "
ROLE_USER = "Entrez le role : "
PASSWORD_USER = "Entrez le mot de passe : "
SERVICE_USER = "Entrez le service : "
S_SOCIAL_USER = "Entrez le numéro de sécurité social : "
EMAIL_USER = "Entrez l'email : "


### Ajout User ###
def add_user():
    print(AJOUT_USER)
    matricule = " "
    nom = input(NOM_USER)
    prenom = input(PRENOM_USER)
    ville = input(VILLE_USER)
    numero = input(NUMERO_USER)
    role = input(ROLE_USER)
    password = input(PASSWORD_USER)
    user = U(matricule,nom, prenom, ville, numero, role, password)
    user.set_mat_user(SqlRequest.countmatricule()+1)
    SqlRequest.insert_user(user)
    print(AJOUT_OK)
    return user

### Ajout User PH ###
def add_user_ph():
    print(AJOUT_USER)
    matricule = " "
    nom = input(NOM_USER)
    prenom = input(PRENOM_USER)
    ville = input(VILLE_USER)
    numero = input(NUMERO_USER)
    service = input(SERVICE_USER)
    role = input(ROLE_USER)
    password = input(PASSWORD_USER)
    ph = PH(matricule,nom, prenom, ville, numero, service, role, password)
    ph.set_mat_user(SqlRequest.countmatricule()+1)
    SqlRequest.insert_user_ph(ph)
    print(AJOUT_OK)
    return ph

### Ajout User Patient ###
def add_user_patient():
    print(AJOUT_USER)
    matricule = " "
    nom = input(NOM_USER)
    prenom = input(PRENOM_USER)
    ville = input(VILLE_USER)
    numero = input(NUMERO_USER)
    s_social = input(S_SOCIAL_USER)
    role = input(ROLE_USER)
    password = input(PASSWORD_USER)
    patient = P(matricule,nom, prenom, ville, numero, s_social, role, password)
    patient.set_mat_user(SqlRequest.countmatricule()+1)
    SqlRequest.insert_user_patient(patient)
    print(AJOUT_OK)
    return patient

### Affichage User ###
def afficher_user():
    email = input(EMAIL_USER)
    res = SqlRequest.select_user(email)
    if res:
        print("Utilisateur trouvé")
        print("Nom: ", res[0][1])
        print("Prénom: ", res[0][2])
        print("Matricule: ", res[0][0])
        print("Ville: ", res[0][3])
        print("Numéro: ", res[0][4])
        print("Email: ", res[0][5])
        print("Login: ", res[0][6])
        print("Role: ", res[0][8])
        if res[0][10] is not None:
            print("Service: ", res[0][10])
        elif res[0][9] is not None:
            print("Numéro de sécurité social: ", res[0][9])
    else:
        print("Utilisateur non trouvé")

### Suppression User ###
def delete_user():
    email = input(EMAIL_USER)
    res = SqlRequest.select_user(email)
    if res:
        print("1. Oui")
        print("2. Non")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            SqlRequest.delete_user(res[0][0])
            print("Utilisateur supprimé")
        elif choice == "2":
            print("Suppression annulée")
        else:
            print("Choix invalide")
            delete_user()
    else:
        print("Utilisateur non trouvé")

def modify_user():
    email = input(EMAIL_USER)
    res = SqlRequest.select_user(email)
    if res:
        print("Modification de l'utilisateur")
        print("1. Nom")
        print("2. Prénom")
        print("3. Ville")
        print("4. Numéro")
        print("5. Email")
        print("6. Login")
        print("7. Password")
        print("8. Role")
        if res[0][10] is not None:
            print("9. Service")
        elif res[0][9] is not None:
            print("9. Numéro de sécurité social")
        print("10. Retour")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            nom = input("Entrez le nouveau nom: ")
            SqlRequest.update_user(res[0][0], "nom", nom)
        elif choice == "2":
            prenom = input("Entrez le nouveau prénom: ")
            SqlRequest.update_user(res[0][0], "prenom", prenom)
        elif choice == "3":
            ville = input("Entrez la nouvelle ville: ")
            SqlRequest.update_user(res[0][0], "ville", ville)
        elif choice == "4":
            numero = input("Entrez le nouveau numéro: ")
            SqlRequest.update_user(res[0][0], "numero", numero)
        elif choice == "5":
            email = input("Entrez le nouvel email: ")
            SqlRequest.update_user(res[0][0], "email", email)
        elif choice == "6":
            login = input("Entrez le nouveau login: ")
            SqlRequest.update_user(res[0][0], "login", login)
        elif choice == "7":
            password = input("Entrez le nouveau mot de passe: ")
            SqlRequest.update_user(res[0][0], "password", password)
        elif choice == "8":
            role = input("Entrez le nouveau role: ")
            SqlRequest.update_user(res[0][0], "role", role)
        elif choice == "9":
            if res[0][10] is not None:
                service = input("Entrez le nouveau service: ")
                SqlRequest.update_user(res[0][0], "service", service)
            elif res[0][9] is not None:
                s_social = input("Entrez le nouveau numéro de sécurité social: ")
                SqlRequest.update_user(res[0][0], "s_social", s_social)

### Menu User ###
def menu_super_admin():
    print("1. Ajouter un utilisateur")
    print("2. Modifier un utilisateur")
    print("3. Afficher un utilisateur")
    print("4. Supprimer un utilisateur")
    print("5. Quitter")
    choice = input("Entrez votre choix: ")
    if choice == "1":
        print("1. Utilisateur")
        print("2. Personnel Hospitalier")
        print("3. Patient")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            add_user()
        elif choice == "2":
            add_user_ph()
        elif choice == "3":
            add_user_patient()
        else:
            print("Choix invalide")
            menu()
    elif choice == "2":
        modify_user()
    elif choice == "3":
        afficher_user()
    elif choice == "4":
        delete_user()
    elif choice == "5":
        print("Au revoir")
    else:
        print("Choix invalide")
        menu_super_admin()

def menu_admin():
    print("1. Ajouter un utilisateur")
    print("2. Modifier un utilisateur")
    print("3. Afficher un utilisateur")
    print("4. Quitter")
    choice = input("Entrez votre choix: ")
    if choice == "1":
        print("1. Utilisateur")
        print("2. Personnel Hospitalier")
        print("3. Patient")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            add_user()
        elif choice == "2":
            add_user_ph()
        elif choice == "3":
            add_user_patient()
        else:
            print("Choix invalide")
            menu()
    elif choice == "2":
        modify_user()
    elif choice == "3":
        afficher_user()
    elif choice == "5":
        print("Au revoir")
    else:
        print("Choix invalide")
        menu_admin()

def menu_utilisateur():
    print("1. Afficher mes informations")
    print("2. Quitter")
    choice = input("Entrez votre choix: ")
    if choice == "1":
        afficher_user()
    elif choice == "2":
        print("Au revoir")
    else:
        print("Choix invalide")
        menu_admin()