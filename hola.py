### condicionales en python


nulos = None
flotantes = 1.2
cadenas = ''
edad = 18
edad_2 = 20

if edad >= 18:
    print('es mayor de edad')
else:
    print('es menor de edad')
    
# listas
frutas = ['naranja', 'manzanas', 'frutilla']
persona = {
    'nombres': 'Juan Jose',
    'apellidos': 'Gonzalez Ramirez'
}

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

# Inmutables
registro_bd = (1, 'Juan', 'Gonzalez')


# Ciclos
for item in frutas:
    print(item)
    

booleanos = True    
cont = 0
while cont < 3:
    print('Hola, estoy en un bucle infinito')
    cont += 1
    #booleanos = False

def soyUnaFuncion(nombre):
    return nombre

    
# POO
class Persona:
    def __init__(self, id, nombres, apellidos, cedula):
        self.id = id
        self.nombre = nombres
        self.apellidos = apellidos
        self.cedula = cedula
    
    # self --> this    
    def mostrarNombre(self):
        print(self.nombre)
        
        
persona1 = Persona(12, 'Roberta', 'Pereira', '6363654')
persona2 = Persona(100, 'Diana', 'Mazier', '8855421')


persona1.mostrarNombre()
print(persona2.id)

print(f"El registro es {persona2.id} y el nombre es {persona2.nombre}")

lista_personas = [persona1, persona2]
for persona in lista_personas:
    print(f"La cedula es {persona.cedula}")




