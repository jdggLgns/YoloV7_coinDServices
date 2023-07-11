import pymysql as pymysql
from Project_properties import conexiones

def getConection():
    con = None
    try:
        con = pymysql.connect(host=conexiones["conn_interna"], user='root', password='coindetection', db='coindetection_database')
    except BaseException as e:
        con = None
    return con
SqlUtils

#Devuelve el id del regidtro creado si se ha insertado correctamente y None en caso contrario
def execInsert(sql, params):
        con = None
        id = None
        try:
            con = getConection()
            cur = con.cursor()
            cur.execute(sql, params)
            id = cur.lastrowid
            con.commit()
        except BaseException as e:
            id = None
        finally:
            if cur:
                cur.close()
            if con:
                con.close()
            return id


def execDelete(sql, params):
    con = None
    all_success = False
    try:
        con = getConection()
        cur = con.cursor()
        cur.execute(sql, params)
        con.commit()
        if cur.rowcount > 0:
            all_success = True
    except BaseException as e:
        all_success = None
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
        return all_success


def execUpdate(sql, params):
    con = None
    all_success = False
    try:
        con = getConection()
        cur = con.cursor()
        cur.execute(sql, params)
        con.commit()
        if cur.rowcount > 0:
            all_success = True
    except BaseException as e:
        all_success = None
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
        return all_success

ç
def execSelect(sql, params):
    con = None
    all_success = False
    try:
        con = getConection()
        cur = con.cursor()
        cur.execute(sql, params)
        rows = cur.fetchall()
    except BaseException as e:
        all_success = None
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
        return rows
