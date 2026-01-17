from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/') 
def index():
    titulo="IDGS804 - Intro Flask"
    listado=['Carlos','Daniel']
    return render_template('index.html', title=titulo, listado=listado)

@app.route('/saludo1')
def saludo1():
    return render_template('saludo1.html')

@app.route('/saludo2')
def saludo2():
    return render_template('saludo2.html')

@app.route('/operasBas')
def operasBas():
    return render_template('operasBas.html')

@app.route('/resultado', methods=['GET', 'POST'])
def resul():
    n1=request.form.get('num1')
    n2=request.form.get('num2')
    return f"<h1>La suma es: {float(n1)+float(n2)}</h1>"



@app.route('/hola')
def func():
    return "Hola Mundo - Hola pequeñuelos"

@app.route("/user/<string:user>") 
def user(user):
    return f'Hola, {user}'

@app.route("/numero/<int:n>") 
def numero(n):
    return f'<h1>Número: {n}</h1>'

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"<h1>Hola {username}, tu id es: {id}</h1>"

@app.route("/suma/<float:n1>/float:n2") 
def suma(n1,n2):
    return f"<h1>la suma es: {n1+n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:parm>")
def func2(parm="Juan"):
    return f"<h1>Hola {parm}</h1>"

@app.route("/operas")
def operas():
    return '''
        <form>
            <label for "name">Name:</label>
            <input type ="text" id="name" name="name" required>
            </br>
            <label for "name">apaterno:</label>
            <input type ="text" id="name" name="name" required>
            </br>
            <input type= "submit" value="Submit">
        </form>
'''

if __name__ =='__main__':
    app.run(debug=True) 