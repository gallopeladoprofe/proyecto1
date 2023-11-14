from flask import Flask, render_template, jsonify
from referencial.ciudad.ciudadDao import CiudadDao

app = Flask(__name__)


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