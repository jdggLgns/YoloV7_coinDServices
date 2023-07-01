import pymysql as pymysql
from Project_properties import conexiones


class GestionUsuarios:
    @staticmethod
    def register(_name, _mail, _userid, _password):
        con = None
        all_success = True
        try:
            if _userid and _password:
                con = pymysql.connect(host=conexiones["conn_interna"], user='root', password='coindetection', db='coindetection_database')
                cur = con.cursor()
                cur.execute("INSERT INTO usuarios (name, mail, userid, password) VALUES (%s, %s, %s, %s)", (_name, _mail, _userid, _password))
                con.commit()
            else:
                all_success = False
        except BaseException as e:
                all_success = False
        finally:
            if con:
                con.close()
            return all_success
