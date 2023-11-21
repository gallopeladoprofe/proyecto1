from flask import Flask, render_template, jsonify, request, redirect, url_for
from referencial.ciudad.ciudadDao import CiudadDao

app = Flask(__name__)


# Render de vistas
@app.route('/index-ciudad')
def index_ciudad():
    cdao = CiudadDao()
    lista = cdao.getCiudades()
    diccionario = []
    if len(lista) > 0:
        for item in lista:
            diccionario.append(
                {
                    'id': item[0],
                    'descripcion': item[1]
                }
            )
    return render_template('vistas_ciudades/index-ciudades.html', ciudades=diccionario)

@app.route('/agregar-ciudad')
def agregar_ciudad():
    return render_template('vistas_ciudades/agregar-ciudad.html')

@app.route('/save-ciudad', methods=['POST'])
def save_ciudad():
    cdao = CiudadDao()
    print(request.form)
    txtciudad = request.form['txtciudad']
    isSaved = False
    if txtciudad != None and len(txtciudad.strip()) > 0:
        isSaved = cdao.insertCiudad(txtciudad.strip().upper())
    if isSaved:
        return redirect(url_for('index_ciudad'))
    else:
        return redirect(url_for('agregar_ciudad'))

# REST
@app.route('/get-ciudad')
def getCiudad():
    cdao = CiudadDao()
    lista = cdao.getCiudades()
    diccionario = []
    if len(lista) > 0:
        for item in lista:
            diccionario.append(
                {
                    'id': item[0],
                    'descripcion': item[1]
                }
            )
        return jsonify(diccionario)
    else:
        return 'no hay ciudades'

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

@app.route('/hija')
def get_hija():
    return render_template('hija.html')

@app.route('/tabla')
def get_tabla():
    return render_template('tabla.html')


if __name__ == '__main__':
    app.run(debug=True)