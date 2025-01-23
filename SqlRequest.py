import ConnectToDb

connect = ConnectToDb.connectdb()

def countmatricule(table=str):
    cursor = connect
    sql = f"SELECT COUNT(matricule) FROM {table};"
    result = cursor.execute(sql)
    print("l'execution a été effectué")
    connect.commit()
    connect.close()
    return result

def insert_user(table=str,matricule=int, nom=str, prenom=str, ville=str, numero=int ,email=str, login=str, password=str,role=str,):
    cursor = connect
    sql = f"INSERT INTO {table} ({matricule},'{nom}', '{prenom}', '{ville}', '{numero}','{email}', {login}',{password}','{role}');"
    cursor.execute(sql)
    print("l'execution a été effectué")
    connect.commit()
    connect.close()

def insertInUserTEST(table=str,is_admin = bool, is_superAdmin = bool , login = str, pwd = str, email= str ):
    cursor = connect
    sql = f"INSERT INTO {table} ({is_admin},{is_superAdmin}, '{login}', '{pwd}', '{email}');"
    cursor.execute(sql)
    print("l'execution a été effectué")
    connect.commit()
    connect.close()

def modifyInPHospitalier(table=str, lastname=str,firstname=str, site=str, service=str ,matricule=int):
    cursor = connect
    sql = f"UPDATE INTO {table} ('{lastname}', '{firstname}', '{site}', '{service}') WHERE matricule = {matricule};"
    cursor.execute(sql)
    print("l'execution a été effectué")
    connect.commit()
    connect.close()

def modifyInUser(table=str,is_admin = bool, is_superAdmin = bool , login = str, pwd = str, email= str , matricule= int):
    cursor = connect
    sql = f"UPDATE INTO {table} ({is_admin}, {is_superAdmin}, '{login}', '{pwd}','{email}' ) WHERE id ={matricule};"
    cursor.execute(sql)
    print("l'execution a été effectué")
    connect.commit()
    connect.close()

def deleteInUser(table=str,is_admin = bool, is_superAdmin = bool , login = str, pwd = str, email= str , matricule= int):
    cursor = connect
    sql = f"DELETE INTO {table} ({is_admin}, {is_superAdmin}, '{login}', '{pwd}','{email}' ) WHERE id ={matricule};"
    cursor.execute(sql)
    print("l'execution a été effectué")
    connect.commit()
    connect.close()

def deleteInPHospitalier(table=str, lastname=str,firstname=str, site=str, service=str ,matricule=int):
    cursor = connect
    sql = f"DELETE INTO {table} ('{lastname}', '{firstname}', '{site}', '{service}') WHERE matricule = {matricule};"
    cursor.execute(sql)
    print("l'execution a été effectué")
    connect.commit()
    connect.close()

def selectInUser(table=str, matricule= int):
    cursor = connect
    sql = f"SELECT * FROM {table}  WHERE id ={matricule};"
    result = cursor.execute(sql)
    print("l'execution a été effectué")
    connect.commit()
    connect.close()
    return result

def selectInPHospitalier(table=str, matricule= int):
    cursor = connect
    sql = f"SELECT * FROM {table}  WHERE matricule ={matricule};"
    result = cursor.execute(sql)
    print("l'execution a été effectué")
    connect.commit()
    connect.close()
    return result
