"""
Proyecto python MySQL:
-Abrir asistente
-Login o registro
-Si elegimos registro, creara un usuario la bbddRe
-Si elegimso login, identifica al usuario y nos preguntará
-Crear nota, mostrar notas, eliminar notas
"""

from usuarios import acciones

print("""  
Acciones disponibles:
    --> Registro    [1]
    --> Login       [2]
""")
#objeto #modulo  #clase
hazEl = acciones.Acciones()
accion = int(input("Qué quieres hacer? \n"))

if accion == 1:
    hazEl.registro()

elif accion == 2:
    hazEl.login()
