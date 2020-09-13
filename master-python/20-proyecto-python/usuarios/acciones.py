from usuarios import usuario as modelo

class Acciones:

    def registro(self):
        
        print("Perfecto vamos a registrarnos en el sistema\n")
        nombre = input("Cual es tu nombre? ")
        apellido = input("Cuales son tus apellidos? ")
        email = input("Cual es tu email? ")
        password = input("Cual es tu password? ")

        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f'Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}')
        
        else:
            print('\nNo te has registrado')
            
    
    def login(self):

        print("Vale !! Identificate en el sistema\n")

        try:
            email = input("Cual es tu email? ")
            password = input("Cual es tu password? ")

            usuario = modelo.Usuario('','', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f'Binevenido {login[1]}, te has identificado en el sistema el día {login[5]}')
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__) #Error en concreto
            print('Login incorrecto, intentalo mas tarde')
    

    def proximasAcciones(self, usuario):
        print(""" 
        -Acciones disponibles:
        -Crear nota          [1]
        -Mostrar tus notas   [2]
        -Eliminar nota       [3]
        -salir               [4]
        """)

        accion = int(input(f'Qué quieres hacer ? '))

        if accion == 1:
            print('Vamos a crear')
            self.proximasAcciones(usuario)

        elif accion == 2:
            print('Vamos a mostrar')
            self.proximasAcciones(usuario)

        elif accion == 3:
            print('Vamos a eliminar')
            self.proximasAcciones(usuario)

        elif accion == 4:
            print('Okey nos vemos en la próxima !! ')
            exit()#Función para salir del programa 
         