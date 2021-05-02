from src.config.db import mysql

class EspacioAcademicoModel:
    def listarEspacios(self):
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM calendario.espacioacd")
        espaciosAcademicos= cursor.fetchall()
        cursor.close()
        return espaciosAcademicos

    def listar_space_ID(self,id):
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM calendario.espacioacd where idespacioacd=%s",(id))
        espaciosAcademicosid= cursor.fetchall()
        cursor.close()
        return espaciosAcademicosid

    def idespacioAcadem(self,espacio):
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT idespacioacd FROM calendario.espacioacd where nombre=%s",(espacio))
        idespacio = cursor.fetchone()
        cursor.close()
        return idespacio
    def crearSpaceAcadem(self,nombre,semestre):
        cursor = mysql.get_db().cursor()
        cursor.execute("INSERT INTO espacioacd(nombre,semestre) values(%s,%s)",(nombre,semestre))
        mysql.get_db().commit()
        cursor.close()

    def editarSpaceAcadem(self,id,nombre,semestre):
        cursor = mysql.get_db().cursor()
        cursor.execute("UPDATE espacioacd set nombre=%s, semestre=%s where idespacioacd=%s",(nombre,semestre,id))
        mysql.get_db().commit()
        cursor.close()

    def eliminarSpaceAcadem(self,id):
        cursor = mysql.get_db().cursor()
        cursor.execute("DELETE FROM espacioacd  where idespacioacd=%s",(id))
        mysql.get_db().commit()
        cursor.close()

