import pymysql as pymysql
from src.Project_properties import conexiones


class GestionUsuarios:
    @staticmethod
    def register(_name, _mail, _userid, _password, con):
        try:
            if _userid and _password:
                con = pymysql.connect(host=conexiones["conn_interna"], user='root', password='coindetection', db='coindetection_database')
                cur = con.cursor()
                cur.execute("INSERT INTO usuarios (name, mail, userid, password) VALUES (%s, %s, %s, %s)", (_name, _mail, _userid, _password))
                con.commit()
            else:
                print("error")
        except BaseException as e:
            print("error " + e)
        finally:
            if con:
                con.close()
