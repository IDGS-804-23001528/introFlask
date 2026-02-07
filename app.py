from flask import Flask, render_template, request, flash
from flask_wtf.csrf import CSRFProtect
import forms
from forms import CinepolisForm
import math

app = Flask(__name__)
app.secret_key = 'Clave secreta'
csrf = CSRFProtect(app)

# --- RUTAS DE NAVEGACIÓN BÁSICA ---

@app.route('/')
def index():
    titulo = "IDGS-802-Flask"
    listado = ['Juan', 'Karla', 'Miguehl']
    return render_template('index.html', titulo=titulo, lista=listado)

@app.route("/formularios")
def formularios():
    return render_template('formularios.html')

@app.route('/reportes')
def reportes():
    return render_template('reportes.html')

@app.route('/alumnos')
def alumnos():
    return render_template('alumnos.html')

# --- EJERCICIOS ---

@app.route('/distancia', methods=["GET", "POST"])
def distancia():
    x1, x2, y1, y2, res = 0, 0, 0, 0, 0
    if request.method == "POST":
        x1 = int(request.form.get("x1"))
        x2 = int(request.form.get("x2"))
        y1 = int(request.form.get("y1"))
        y2 = int(request.form.get("y2"))
        res = math.sqrt(((x2 - x1)**2 + (y2 - y1)**2))
    return render_template('distancia.html', x1=x1, x2=x2, y1=y1, y2=y2, res=res)

@app.route('/usuarios', methods=["GET", "POST"])
def usuarios():
    matricula, nom, apa, ama, correo = 0, '', '', '', ''
    usuarios_class = forms.UserForm(request.form)

    if request.method == "POST" and usuarios_class.validate():
        matricula = usuarios_class.matricula.data
        nom = usuarios_class.nombre.data
        apa = usuarios_class.apaterno.data
        ama = usuarios_class.amaterno.data
        correo = usuarios_class.correo.data

        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)

    return render_template("usuarios.html", form=usuarios_class, matricula=matricula, nom=nom, apa=apa, ama=ama, correo=correo)



app = Flask(__name__)
app.secret_key = 'Clave secreta'
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/cinepolis", methods=["GET", "POST"])
def cinepolis():
    
    Total = 0
    form = forms.CinepolisForm(request.form)
    
    if request.method == "POST" and form.validate():
        nom = form.nombre.data
        cantiCom = form.compradores.data
        isCineco = form.cineco.data  
        cantiBol = form.boletos.data
        
        limit = cantiCom * 7
        
        if cantiBol <= limit:
            Total = cantiBol * 12
           
            if 3 <= cantiBol <= 5:
                Total *= 0.90
            elif cantiBol > 5:
                Total *= 0.85
            
            
            if isCineco == "si" or isCineco == "true":
                Total *= 0.88
        else:
            Total = 0
            flash("Solo se permiten 7 boletos por comprador. La cantidad ingresada es incorrecta.")
            
   
    return render_template("cinepolis.html", form=form, Total=Total)

if __name__ == '__main__':
    app.run(debug=True)



@app.route('/hola')
def hola():
    return "Hola al cuadrado!"


@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}!!!!!"


@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

@app.route("/operasBas", methods=["GET", "POST"])
def operas1():
    n1, n2, res, operacion = 0, 0, 0, ''
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        operacion = request.form.get("opera")

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
    return render_template("operasBas.html", operacion=operacion, n1=n1, n2=n2, res=res)

# --- CIERRE DEL ARCHIVO ---

if __name__ == '__main__':

    app.run(debug=True)
