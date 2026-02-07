from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, RadioField
from wtforms import EmailField, validators

class UserForm(Form):
    matricula=IntegerField('Matricula',[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="Ingrese un valor válido")
    ])
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un nombre válido")
    ])
    apaterno=StringField('Apaterno', [
        validators.DataRequired(message="El campo es requerido")
    ])
    amaterno=StringField('Amaterno', [
        validators.DataRequired(message="El campo es requerido")
    ])
    correo=StringField('Correo', [
        validators.Email(message="Ingrese un correo válido")
    ])

from wtforms import Form, StringField, IntegerField, RadioField, validators

class CinepolisForm(Form):
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un nombre valido")
    ])
    compradores = IntegerField('Cantidad Compradores',[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, message="Ingrese un valor valido")
        ])
    cineco = RadioField('Es Cineco', choices=[('no','No'),('si','Si')])
    boletos = IntegerField('Cantidad Boletos',[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, message="Ingrese un valor valido")
        ])