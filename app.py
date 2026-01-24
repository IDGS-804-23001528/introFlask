from flask import Flask, render_template, request
import math
import forms
from flask_wtf.csrf import CSRFProtect 

app = Flask(__name__)
app.secret_key = 'clave_secreta'
csrf = CSRFProtect()


# Renderizamos un archivo estático html [DEBE ESTAR EN LA CARPETA TEMPLEATES]
@app.route('/')
def index():
    titulo="IDGS-804-Flask"
    listado=['Carlos', 'Oscar', 'Miguel']
    return render_template('index.html', titulo=titulo, lista=listado)

# Ruta para otra página
@app.route("/formularios")
def formularios():
    return render_template('formularios.html')

@app.route('/reportes')
def reportes():
    return render_template('reportes.html')


@app.route('/distancia', methods=["GET", "POST"])
def distancia():
    x1=0
    x2=0
    y1=0
    y2=0
    res=0
    if request.method == "POST":
        x1=int(request.form.get("x1"))
        x2=int(request.form.get("x2"))
        y1=int(request.form.get("y1"))
        y2=int(request.form.get("y2"))
        res = math.sqrt(((x2 - x1)*(x2-x1) + (y2 - y1)*(y2 - y1)))
    return render_template('distancia.html',x1=x1,x2=x2,y1=y1,y2=y2,res=res)

# Otra ruta que tiene un metodo que retorna un saludo
@app.route('/hola')
def hola():
    return "Hola al cuadrado!"

# Podemos poner una variable en la ruta
@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}!!!!!"
# f"mensaje {user}"" es igual a .format(user)

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "ID: {} nombre: {}".format(id, username)

@app.route("/suma/<float:n1>/<float:n2>")
def func(n1,n2):
    return "La suma es: {}".format(n1+n2)

# Se sobreescribe el valor si existe
@app.route("/default/")
@app.route("/default/<string:param>")
def function(param="juan"):
    return f"<h1>¡Hola, {param}!<h1>"

@app.route("/operas")
def operas():
    return '''
        <form>
            <label for="name">Nombre:</label>
            <input type="text" id="name" name="name" required>

            <label for="appP">Apellido Paterno:</label>
            <input type="text" id="appP" name="appP" required>
        </form>
    '''

@app.route("/operasBas",  methods=["GET", "POST"])
def operas1():
    n1=0
    n2=0
    res=0
    operacion=''
    if request.method == "POST":
        n1=request.form.get("n1")
        n2=request.form.get("n2")
        operacion=request.form.get("opera")

    if operacion == "suma":
        res = float(n1) + float(n2)
    elif operacion == "resta":
        res = float(n1) - float(n2)
    elif operacion == "multip":
        res = float(n1) * float(n2)
    elif operacion == "division":
        res = float(n1) / float(n2)
    else:
        res = 0
    return render_template("operasBas.html",operacion=operacion,n1=n1,n2=n2,res=res)

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    n1=request.form.get("n1")
    n2=request.form.get("n2")
    operacion=request.form.get("opera")

    if operacion == "suma":
        res = float(n1) + float(n2)
    elif operacion == "resta":
        res = float(n1) - float(n2)
    elif operacion == "multip":
        res = float(n1) * float(n2)
    elif operacion == "division":
        res = float(n1) / float(n2)
    else:
        res = 0
    return f"El resultado de la operación {operacion} es: {res}"


@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    mat=0
    nom=''
    ape=''
    email=''
    alumno_clas=forms.userForm(request.form)
    if request.method=='POST' and alumno_clas.validate():
        mat=alumno_clas.matricula.data
        nom=alumno_clas.nombre.data 
        ape=alumno_clas.apellido.data
        email=alumno_clas.correo.data
    return render_template('alumnos.html',form=alumno_clas,mat=mat,nom=nom,ape=ape,email=email)

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)
