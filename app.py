from flask import Flask, render_template, request, session, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

# Set palabra clave
app.secret_key = b'mipalabrasecreta'

# Agregando endpoints para login
@app.route('/')
def index():
    if 'usuario' in session:
        return f'Sesión logueada correctamente, eres {session["usuario"]}'
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        print(request.form)
        usuario = request.form['usuario']
        clave = request.form['clave']
        if usuario == 'juan' and clave == '1':
            session['usuario'] = usuario
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

# endpoint
@app.route('/hola')
def hola():
    lista_personas = [
    {
        'nombres': 'Juan Jose',
        'apellidos': 'Gonzalez Ramirez'
    }, 
    {
        'nombres': 'Sandra',
        'apellidos': 'Lopez'
    }
]
    return lista_personas

@app.route('/ver-documento/<int:documento>')
def ver_documento(documento):
    return f"mi ci es {documento}"

@app.route('/ver-html')
def ver_html():
    # Server side rendering
    # Client side rendering
    usuario = 'ADMINISTRADO POR SU SUEGRA'
    return render_template('index.html', usuario=usuario)

@app.route('/ciudad')
def get_ciudad():
    ciudades = [{
        'id': '01', 'descripcion': 'Asunción'
        },
        {
            'id': '02', 'descripcion': 'Limpio'
        },
        {
            'id': '03', 'descripcion': 'Fernando de la Mora'
        },
        {
            'id': '04', 'descripcion': 'Villa Elisa'
        }
    ]
    return render_template('vistas_ciudades/ver-ciudades.html', ciudades=ciudades)

@app.route('/hija')
def get_hija():
    return render_template('hija.html')

@app.route('/tabla')
def get_tabla():
    return render_template('tabla.html')


if __name__ == '__main__':
    app.run(debug=True)