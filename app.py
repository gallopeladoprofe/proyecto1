from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

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
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)