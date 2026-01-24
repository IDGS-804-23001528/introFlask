from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField
from wtforms import validators

class userForm(FlaskForm):
    matricula = IntegerField('Matricula', [
        validators.DataRequired(message='La matricula es requerida')
    ])

    nombre = StringField('Nombre', [
        validators.DataRequired(message='El campo nombre es requerido')
    ])

    apellido = StringField('Apellido', [
        validators.DataRequired(message='El campo apellido es requerido')
    ])

    correo = EmailField('Correo', [
        validators.DataRequired(message='El campo correo es requerido')
    ])