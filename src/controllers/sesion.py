from flask import render_template, request, redirect, url_for, jsonify
from src import app
from src.models.mdsSesion import SesionModel
from src.models.mdsSpaceAcad import EspacioAcademicoModel
from src.models.mdsEstudiantes import EstudianteModel
sesionModel = SesionModel()
espacioModel = EspacioAcademicoModel()
estudianteModel = EstudianteModel()
@app.route('/sesiones', methods=['GET','POST'])
def seciones():
    sesiones = sesionModel.listarSesion()
    espacios = espacioModel.listarEspacios()
    return render_template('sesion/sesion.html',sesiones=sesiones, espacios=espacios)


@app.route('/sesiones/crear', methods=['GET','POST'])
def agregarSesion():
    if request.method == 'POST':
        fecha = request.form['fecha']
        hora_inicio = request.form['hora_inicio']
        hora_final = request.form['hora_final']
        materia = request.form['espacioacademico']
        sesionModel.crearSesion(fecha, hora_inicio,hora_final,materia)
        idsesion = sesionModel.idsesion()
        falta=1
        print("id sesion:",idsesion)
        estudiante = estudianteModel.idAllstudiantes(materia)
        for estudent in estudiante:
            for i in estudent:
                sesionModel.sesionEtudiane(idsesion,i,falta)
                print("idestudiate",i)
            
        print(estudiante)
        return  redirect(url_for('seciones'))
    else:
        return redirect(url_for('seciones'))

@app.route('/sesiones/materia/<idsesion>', methods=['GET','POST','PUT'])
def sesionMateria(idsesion):
    id=idsesion
    estudianteSesion = sesionModel.estudianteListMateria(idsesion)
    if request.method == 'GET':
        print(estudianteSesion)
        print(idsesion)
        return render_template("sesion/listarEstudianteSesion.html",estudianteSesions=estudianteSesion,id=idsesion)
    elif request.method == 'POST':
        
        data = request.form['inlineRadioOptions']
        datos = data.split(',')
        f=0
        v=1
        idstudiante = int(datos[0])
        asistencia = int(datos[1])
        select = datos[2]
        print(data)
        if select == "+":
            print("op mas",v)
            
            sesionModel.editarEstudianteMateria(idstudiante,v)
            estudianteSesion = sesionModel.estudianteListMateria(idsesion)
            return render_template("sesion/listarEstudianteSesion.html",estudianteSesions=estudianteSesion,id=idsesion)
        elif select =="-":
            print("op menors",f)
            
            sesionModel.editarEstudianteMateria(idstudiante,f)
            estudianteSesion = sesionModel.estudianteListMateria(idsesion)
            return render_template("sesion/listarEstudianteSesion.html",estudianteSesions=estudianteSesion,id=idsesion)

@app.route('/sesiones/editar/<int:id>', methods=['GET'])
def editarsesion(id):
    if request.method =="GET":
        #espacios = espacioModel.listarEspacios()
        datosesiones = sesionModel.id_sesion(id)
        print(datosesiones)
        return render_template("sesion/editarSesion.html",datosesiones=datosesiones)

@app.route('/sesiones/actualizado', methods=['POST'])
def actualizarSesion():
    if request.method =="POST":
        idseesion =int( request.form['idsesion'])
        fecha = request.form['fecha']
        hora_inicio = request.form['hora_inicio']
        hora_final = request.form['hora_final']

        sesionModel.editarSesion(idseesion,fecha,hora_inicio,hora_final)
        return redirect(url_for('seciones'))

@app.route('/sesiones/eliminar/<int:id>')
def eliminar_sesion(id):
    sesionModel.eliminarSesion(id)
    return redirect(url_for('seciones'))


 
        


