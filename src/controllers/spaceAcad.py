from flask import render_template, request, redirect, url_for, jsonify
from src import app
from src.models.mdsSpaceAcad import EspacioAcademicoModel

espacioModel = EspacioAcademicoModel()

@app.route('/space-academic', methods=['GET'])
def listar_space():
    if request.method == 'GET':
        space_academico = espacioModel.listarEspacios()
        return render_template('spaceAcademico/listarSpace.html',spaces=space_academico)

@app.route('/space/editar/<int:id>', methods=['POST','GET'])
def editar_spacio(id):
    if request.method == 'GET':
        space_academico = espacioModel.listar_space_ID(id)
        return render_template('spaceAcademico/editarSpace.html',spaces=space_academico)

@app.route('/space/actualizado', methods=['POST'])
def actualizar_space():
    id= int(request.form['id'])
    nombre = request.form['materia']
    semestre = request.form['semestre']
    espacioModel.editarSpaceAcadem(id,nombre,semestre)
    return redirect(url_for('listar_space'))

@app.route('/space/crear', methods=['GET','POST'])
def crear_space():
    if request.method =='GET':
        return render_template("spaceAcademico/crearSpace.html")
    else:
        nombre = request.form['materia']
        semestre = request.form['semestre']
        espacioModel.crearSpaceAcadem(nombre,semestre)
        return redirect(url_for('listar_space'))

@app.route('/space/eliminar/<int:id>')
def eliminar_space(id):
    espacioModel.eliminarSpaceAcadem(id)
    return redirect(url_for('listar_space'))

 