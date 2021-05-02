from flask import render_template, request, redirect, url_for, jsonify
from src import app
from src.models.mdsEstudiantes import EstudianteModel
from src.models.mdsSpaceAcad import EspacioAcademicoModel
estudianteModel = EstudianteModel()
espaciosAcademico = EspacioAcademicoModel()
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/estudiante', methods=['GET'])
def listaStudents():
    estudiante = estudianteModel.listarEstudiantes()
    print(estudiante)
    return render_template('estudiante/listaStudent.html',estudents=estudiante)

@app.route('/estudiante/crear', methods=['GET','POST'])
def crearStudents():
    if request.method == 'GET':
        espacioacd = espaciosAcademico.listarEspacios()
        return render_template('estudiante/crearEstudent.html',espacios=espacioacd)
    else:
        #estudiante = estudianteModel.listarEstudiantes()
        cc = request.form['Identificacion']
        nombre = request.form['Nombre']
        apellido = request.form['Apellido']
        celular = request.form['Celular']
        correo = request.form['Correo']
        semestre = request.form['semestre']
        espacio = int(request.form['espacioacademico'])
        
        estudianteModel.crearEstudiante(cc,nombre,apellido,celular,correo,semestre,espacio)
        return redirect(url_for("listaStudents"))

@app.route("/update/<int:id>", methods =['POST','GET'])
def get_student(id):
    
    estudiante = estudianteModel.get_student(id)
    #print(estudiante[0][1])
        
    return render_template('estudiante/editarStudent.html', estudiante = estudiante)
#------------------------------------ENPOINT
@app.route("/estudiante_actualizado", methods =['POST'])
def actualizar_estudiante():
    
    if request.method == 'POST':

        id_ = request.form['id_']
        cc = request.form['Identificacion']
        nombre = request.form['Nombre']
        apellido = request.form['Apellido']
        celular = request.form['Celular']
        correo = request.form['Correo']

        estudianteModel.update_student(str(id_),str(cc),str(nombre),str(apellido),str(celular),str(correo))
    
        return redirect(url_for('listaStudents'))

@app.route("/delete/<int:id>")
def eliminar_estudiante(id):
    estudianteModel.delete_student(id)
    return redirect(url_for('listaStudents'))