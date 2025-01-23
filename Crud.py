from User import User as U
from User import PHospitalier as PH
from User import Patient as P
import SqlRequest
import sqlite3


### Ajout User ###
def add_user(self):
    print("Ajout d'un utilisateur")
    nom = input("Entrez le nom: ")
    # if nomvalid.set_nom(nom) == False:
    #     print("Le nom est invalide")
    prenom = input("Entrez le prénom: ")
    mat_user = U.gen_mat_user(self) 
    ville = input("Entrez la ville: ")
    email = U.gen_email(self)
    login = U.gen_login(self)
    password = U.gen_password(self)
    role = input("Entrez le role: ")
    user = U.User(nom, prenom, mat_user, ville, email, login, password,role)
    self.U.insertInUser(user)
    print("Utilisateur ajouté")
    return self.User

### Ajout User PHospitalier ###
def add_user_ph(self):
    print("Ajout d'un utilisateur")
    nom = input("Entrez le nom: ")
    # nomValid = User(nom)
    # if nomValid.set_nom(nom) == False:
    #     print("Le nom est invalide")
    prenom = input("Entrez le prénom: ")
    mat_user = U.gen_mat_user(self) 
    ville = input("Entrez la ville: ")
    email = U.gen_email(self)
    login = U.gen_login(self)
    password = U.gen_password(self)
    role = input("Entrez le role: ")
    service = input("Entrez le service: ")
    user = U.User(nom, prenom, mat_user, ville, email, login, password,role,service)
    userph = PH.UserPHospitalier(mat_user,service)
    self.U.insertInUser(user)
    self.U.insertInPHospitalier(userph)
    print("Utilisateur ajouté")
    return self.User

# ### Modification User ###
# def modify_User(self, Etudiant):
#     print("Modification de l'utilisateur")
#     print("1. Nom")
#     print("2. Prénom")
#     print("3. Numéro d'étudiant")
#     print("4. Année d'étude")
#     print("5. Filière")
#     print("6. Classe")
#     print("7. Absences")
#     print("8. Email")
#     print("9. login")
#     print("10. Password")
#     print("11. Retour")
#     choice = input("Entrez votre choix: ")
#     if choice == "1":
#         Etudiant.set_nom(input("Entrez le nouveau nom: "))
#     elif choice == "2":
#         Etudiant.set_prenom(input("Entrez le nouveau prénom: "))
#     elif choice == "3":
#         Etudiant.set_num_etudiant(input("Entrez le nouveau numéro d'étudiant: "))
#     elif choice == "4":
#         Etudiant.set_aScolaire(input("Entrez la nouvelle année d'étude: "))
#     elif choice == "5":
#         Etudiant.set_filière(input("Entrez la nouvelle filière: "))
#     elif choice == "6":
#         Etudiant.set_classe(input("Entrez la nouvelle classe: "))
#     elif choice == "7":
#         Etudiant.set_absence(input("Entrez le nouveau nombre d'absences: "))
#     elif choice == "8":
#         Etudiant.set_email(input("Entrez le nouvel email: "))
#     elif choice == "9":
#         Etudiant.set_login(input("Entrez le nouveau login: "))
#     elif choice == "10":
#         Etudiant.set_password(input("Entrez le nouveau mot de passe: "))
#     elif choice == "11":
#         modify_User(self, Etudiant)

# ### Suppression User ###
# def delete_User(self, Etudiant):
#     print("Suppression de l'utilisateur")
#     print("1. Oui")
#     print("2. Non")
#     choice = input("Entrez votre choix: ")
#     if choice == "1":
#         self.Etudiants.remove(Etudiant)
#         print("Utilisateur supprimé")
#     elif choice == "2":
#         print("Suppression annulée")
#     else:
#         print("Choix invalide")
#         delete_User(self, Etudiant)
#     return self.Etudiants

# ### Affichage User ###
# def afficher_User(self, Etudiant):
#     print("--------------------")
#     print("Affichage de l'utilisateur")
#     print("Nom: ", Etudiant.get_nom())
#     print("Prénom: ", Etudiant.get_prenom())
#     print("Numéro d'étudiant: ", Etudiant.get_num_etudiant())
#     print("Année d'étude: ", Etudiant.get_aScolaire())
#     print("Filière: ", Etudiant.get_filière())
#     print("Classe: ", Etudiant.get_classe())
#     print("Absences: ", Etudiant.get_absence())
#     print("Email: ", Etudiant.get_email())
#     print("Login: ", Etudiant.get_login())
#     print("--------------------")


# def afficher_allUser(self):
#     print("--------------------")
#     print("Affichage de tous les utilisateurs")
#     for Etudiant in self.Etudiants:
#         print("Nom: ", Etudiant.get_nom())
#         print("Prénom: ", Etudiant.get_prenom())
#         print("Numéro d'étudiant: ", Etudiant.get_num_etudiant())
#         print("Année d'étude: ", Etudiant.get_aScolaire())
#         print("Filière: ", Etudiant.get_filière())
#         print("Classe: ", Etudiant.get_classe())
#         print("Absences: ", Etudiant.get_absence())
#         print("Email: ", Etudiant.get_email())
#         print("Login: ", Etudiant.get_login())
#         print("--------------------")


# ### Menu User ###
# def menu_User(self):
#     print("1. Ajout d'un utilisateur")
#     print("2. Modification d'un utilisateur")
#     print("3. Suppression d'un utilisateur")
#     print("4. Affichage d'un utilisateur")
#     print("5. Affichage de tous les utilisateurs")
#     print("6. Retour")
#     choice = input("Entrez votre choix: ")
#     if choice == "1":
#         add_User(self)
#     elif choice == "2":
#         nom = input("Entrez le nom de l'étudiant: ")
#         for Etudiant in self.Etudiants:
#             if Etudiant.get_num_etudiant() == num_etudiant:
#                 modify_User(self, Etudiant)
#                 break
#         else:
#             print("Utilisateur non trouvé")
#     elif choice == "3":
#         nom = input("Entrez le nom de l'étudiant: ")
#         for Etudiant in self.Etudiants:
#             if Etudiant.get_num_etudiant() == num_etudiant:
#                 delete_User(self, Etudiant)
#                 break
#         else:
#             print("Utilisateur non trouvé")
#     elif choice == "4":
#         nom = input("Entrez le nom de l'étudiant: ")
#         for Etudiant in self.Etudiants:
#             if Etudiant.get_num_etudiant() == num_etudiant:
#                 afficher_User(self, Etudiant)
#                 break
#         else:
#             print("Utilisateur non trouvé")
#     elif choice == "5":
#         afficher_allUser(self)
#     elif choice == "6":
#         return
#     else:
#         print("Choix invalide")
#         menu_User(self)
#     menu_User(self)


