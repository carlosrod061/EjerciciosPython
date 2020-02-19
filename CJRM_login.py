def login(user,password):
    usuario = "utng"
    contrasenia = "mexico"
    
    if user==usuario and password==contrasenia :
        print("Bienvenido")
    
    else:
        print("Datos incorrectos")




user = (input("Escriba el usuario \n"))
password = (input("Escriba la contrasenia \n"))
login(user,password)

input("")