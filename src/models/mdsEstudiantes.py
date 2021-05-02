from src.config.db import mysql

class EstudianteModel():
    def listarEstudiantes(self):
        cursor = mysql.get_db().cursor()
        cursor.execute("""
        SELECT 
        estudiantes.idestudent,
        estudiantes.identificacion,
        estudiantes.nombre,
        estudiantes.apellido,
        estudiantes.celular,
        estudiantes.correo,
        estudiantes.semestre, 
        espacioacd.nombre 
        FROM 
        calendario.estudiantes,espacioacd 
        where 
        estudiantes.idespacioacd=espacioacd.idespacioacd
        """)
        estudiantes= cursor.fetchall()
        cursor.close()
        print(estudiantes)
        return estudiantes
        
    def crearEstudiante(self,cc,nombre,apellido,celular,correo,semestre,espacioacd):
        cursor = mysql.get_db().cursor()    
        cursor.execute("""insert into estudiantes(identificacion,nombre,apellido,celular,correo,semestre,idespacioacd)
                        values(%s,%s,%s,%s,%s,%s,%s)
                        """,(cc,nombre,apellido,celular,correo,semestre,espacioacd))
        mysql.get_db().commit()
        cursor.close()
    def idAllstudiantes(self,materia):
        cursor = mysql.get_db().cursor() 
        cursor.execute("""SELECT idestudent FROM calendario.estudiantes,calendario.espacioacd
                         WHERE estudiantes.idespacioacd=espacioacd.idespacioacd 
                         and espacioacd.nombre=%s""",(materia))
        idAllestudiantes= cursor.fetchall()
        cursor.close()
        return idAllestudiantes

    def update_student(self,id_,cc,nombre,apellido,celular,correo):

        cursor = mysql.get_db().cursor()
        cursor.execute('UPDATE estudiantes SET identificacion=%s, nombre=%s, apellido=%s, celular=%s, correo=%s WHERE idestudent=%s',(cc,nombre,apellido,celular,correo, id_))
        estudiantes = cursor.fetchall()
        mysql.get_db().commit()
        cursor.close()
    
    def get_student(self, id_):

        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM estudiantes where estudiantes.idestudent=" + str(id_))
        
        estudiante = cursor.fetchall()
        cursor.close()
        return estudiante

    def delete_student(self, id):
        cursor = mysql.get_db().cursor()
        cursor.execute("delete from estudiantes where idestudent = %s",(id,))
        mysql.get_db().commit()
        cursor.close()