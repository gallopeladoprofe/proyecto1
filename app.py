from flask import Flask, render_template, jsonify, request, redirect, url_for
from referencial.ciudad.ciudadDao import CiudadDao
from referencial.persona.personaDao import PersonaDao

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')
    

# Render de vistas

# personas
@app.route('/index-persona')
def index_persona():
    return render_template('gestionar_referenciales/vistas_personas/index-persona.html')

# Operaciones REST[GET, POST, PUT, PATCH, DELETE]
@app.route('/save-persona', methods=['POST'])
def save_persona():
    
    nombres = request.json['nombres']
    apellidos = request.json['apellidos']
    cedula = request.json['cedula']
    direccion = request.json['direccion']
    
    guardado = False
    
    if len(nombres.strip()) > 0 and len(apellidos.strip()) > 0 and len(apellidos.strip()) > 0:
        pers =  PersonaDao()
        guardado = pers.insertPersona(nombres.strip().upper(), apellidos.strip().upper(), cedula.strip(), direccion.strip())
        if guardado:
            return jsonify({
                'success': 'Se guardo el registro',
                'error': None
            })
        else:
            return jsonify({
                'success': None,
                'error': 'No se pudo guardar el registro'
            })
    else:
        return jsonify({
                'success': None,
                'error': 'No se envio correctamente el post'
            })
        

# ciudades
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
    txtciudad = request.form['txtciudad']
    isSaved = False
    if txtciudad != None and len(txtciudad.strip()) > 0:
        isSaved = cdao.insertCiudad(txtciudad.strip().upper())
    if isSaved:
        return redirect(url_for('index_ciudad'))
    else:
        return redirect(url_for('agregar_ciudad'))

@app.route('/editar-ciudad/<id>')
def editar_ciudad(id):
    cdao = CiudadDao()
    ciudadFound = cdao.getCiudadById(id)
    if ciudadFound:
        return render_template('vistas_ciudades/editar-ciudad.html', ciudad=ciudadFound)
    return redirect(url_for('index_ciudad'))

@app.route('/update-ciudad', methods=['POST'])
def update_ciudad():
    cdao = CiudadDao()
    idtxtciudad = request.form['idtxtciudad']
    txtciudad = request.form['txtciudad']
    isUpdated = False
    if idtxtciudad == None or len(idtxtciudad.strip()) == 0:
        return redirect(url_for('index_ciudad'))
    
    if txtciudad != None and len(txtciudad.strip()) > 0:
        isUpdated = cdao.updateCiudad(idtxtciudad.strip(), txtciudad.strip().upper())
    if isUpdated:
        return redirect(url_for('index_ciudad'))
    else:
        return redirect(url_for('editar_ciudad', id=idtxtciudad))

@app.route('/delete-ciudad/<id>')
def delete_ciudad(id):
    cdao = CiudadDao()
    cdao.deleteCiudad(id)
    return redirect(url_for('index_ciudad'))

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