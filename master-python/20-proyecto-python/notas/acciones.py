import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f'\nOk {usuario[1]}!! vamos a crear una nota... ')

        titulo = input("Ingresa el titulo de la nota: ")
        descripcion = input("Ingresa la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f'Perfecto la nota {nota.titulo} se ah guardado')
        else:
            print(f'La nota no se ah guardado, lo siento {usuario[1]}')
        return guardar