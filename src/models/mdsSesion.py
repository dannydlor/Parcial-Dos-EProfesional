from src.config.db import mysql

class SesionModel():
    def listarSesion(self):
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM calendario.sesiones")
        sesiones = cursor.fetchall()
        cursor.close()
        return sesiones

    def crearSesion(self,fecha, hora_inicio,hora_final,materia):
        cursor = mysql.get_db().cursor()
        cursor.execute("INSERT into calendario.sesiones(fecha,hora_inicio,hora_final, asignatura) values(%s, %s, %s,%s)",(fecha,hora_inicio,hora_final,materia))
        mysql.get_db().commit()
        cursor.close()
    def idsesion(self):
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT idsesiones FROM calendario.sesiones ORDER by idsesiones DESC LIMIT 1")
        sesiones = cursor.fetchone()
        cursor.close()
        return sesiones
    def sesionEtudiane(self,idsesion,i,falta):
        cursor = mysql.get_db().cursor()
        cursor.execute("INSERT into calendario.sesion_estudiantes(idsesion,idestudiante,asistencia) values (%s,%s,%s)",(idsesion,i,falta))
        mysql.get_db().commit()
        cursor.close()
    def estudianteListMateria(self,idsesion):
        cursor = mysql.get_db().cursor()
        cursor.execute(""" select idestudent,identificacion,nombre,apellido,celular,asistencia 
                            from calendario.estudiantes,calendario.sesiones,calendario.sesion_estudiantes
                            where idsesion=idsesiones and idestudiante=idestudent  
                            and idsesion=%s""",(idsesion))
        estudianteMateria = cursor.fetchall()
        cursor.close()
        return estudianteMateria
    
    def editarEstudianteMateria(self,idstude,asistencia):
        cursor = mysql.get_db().cursor()
        cursor.execute("UPDATE calendario.sesion_estudiantes set asistencia = %s WHERE idestudiante = %s",(asistencia,idstude))
        print("mysql:",idstude,asistencia)
        mysql.get_db().commit()
        cursor.close()
    
    def id_sesion(self,id):
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM calendario.sesiones WHERE idsesiones=%s",(id))
        id_sesions = cursor.fetchall()
        cursor.close()
        return id_sesions

    def eliminarSesion(self,id):
        cursor = mysql.get_db().cursor()
        cursor.execute("DELETE FROM calendario.sesiones WHERE idsesiones = %s",(id))
        mysql.get_db().commit()
        cursor.close()

    def editarSesion(self,id,fecha,hora_inicio,hora_final):
        cursor = mysql.get_db().cursor()
        cursor.execute("UPDATE sesiones SET fecha =%s, hora_inicio = %s, hora_final=%s  where idsesiones=%s",(fecha,hora_inicio,hora_final,id))
        mysql.get_db().commit()
        cursor.close()