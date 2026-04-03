usuario_correcto = "alumno"
clave_correcta = "python123"

usuario = ""
clave = ""
intentos = 3
contador = 0

acceso = True

clave_actualizada = False
while acceso:
           
    contador += 1
  
    if contador <= intentos:
        usuario = input("\nIngresar nombre de usuario: ").strip()
        clave = input("Ingresar clave de usuario: ").strip()
        
        print(f"\nIntento {contador}/{intentos} - Usuario: {usuario}")
        print("Clave ingresada")
        if usuario == usuario_correcto and clave == clave_correcta:
            print("Acceso concedido.") 
            acceso = False
        else:
            print("Error: credenciales inválidas.")    
    else:    
        acceso = False    
        print("""Cuenta bloqueada""")
# print(contador)
   
entrarMenu = True
while entrarMenu and contador <= intentos:
        
    menu = input("\n - 1) Estado - 2) Cambiar clave - 3) Mensaje - 4) Salir\nOpcion: ")
    while not menu.isdigit():
        print(f"Opción: {menu} ")
        print("Error: ingrese un número válido. ")    
        menu = input("Intentar otra vez: ")             
    menu = int(menu)  
   
    match menu:
        case 1: 
            print("\nEstado: ")
            print(f"- Login: {usuario}\n- Conectado")
            if clave_actualizada:
                print("- Clave: actualizada")
            else:
                print("- Clave: sin cambios")
        case 2:
            print("\nCambiar clave")
            cantCaractClave = 6
            clave = input(f"Ingresar nueva clave minimo {cantCaractClave} caracteres y alfanumerica: ")
            while not clave.isalnum() or len(clave) < int(cantCaractClave):
            #    print(f"Nueva clave: {clave}")
                clave = input(f"Error: mínimo {cantCaractClave} caracteres. : ")
            clave_correcta = clave
            clave = ""
            clave_actualizada = True        
        case 3:
            print("\nMensaje")
            print(f"A la espera {usuario} de agregar contenido")
        case 4: 
            print("\nSalir")
            entrarMenu = False
        case _: 
            print(f"\nOpción: {menu} ")
            print("Error: opción fuera de rango. ")
      

    
