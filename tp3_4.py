energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzarCerradura = 0

inicioJuego = True

contador = 1 

print("\n========================\nEscape Room: La Bóveda\n========================")

personaje = input("Ingresar nombre del personaje: ")
while not personaje.isalpha():
    personaje = input("Solo letras, intentar otra vez: ")
    
while inicioJuego:
    print("\n~~~~~~~~~~~~\nEstadisticas\n~~~~~~~~~~~~")
    print(f"### Energia: {energia} ### Tiempo: {tiempo} ### Cerraduras Abiertas: {cerraduras_abiertas} ###")
    print(f"Cerraduras Forzadas: {forzarCerradura}/3 - Alarma (Bloqueo): {alarma} - Codigo parcial: {codigo_parcial} ")
    
    print("\n1. Forzar cerradura\n2. Hackear panel\n3. Descansar") 

    menuJuego = input("Ingresar un Opción: ")   
    while not menuJuego.isdigit() or not (0 < int(menuJuego) < 4):
        menuJuego = input("Imgresar un numero (1 al 3): ")
    menuJuego = int(menuJuego)

    match menuJuego:    
        case 1:
            print("\nForzar cerradura (costo: -20 energía, -2 tiempo)\n")
            energia -= 20
            tiempo -= 2
                 
            if forzarCerradura >= 2:
                print("\nAnti Spam")
                alarma = True 
                
                print(f"--- Alarma activada - Cerraduras Bloqueadas --- \n")

            elif forzarCerradura < 2:
                forzarCerradura += 1 
                print(f"Cerraduras Forzadas: {forzarCerradura}/3")
                numElegido = input("Ingresar un N.ro del 1 al 3: ")
                while not numElegido.isdigit() or not (0 < int(numElegido) < 4):
                    numElegido = input("\nIngresar un numero: ")
                numElegido = int(numElegido)    
                
                print("\n“Riesgo de alarma”\n") 
                if energia < 40 and numElegido == 3:
                    alarma = True
                else:
                    cerraduras_abiertas  += 1          
                      
   
        case 2:
            print("Hackear panel (costo: -10 energía, -3 tiempo)")
            energia -= 10
            tiempo -= 3

            forzarCerradura = 0
            if alarma: # Opcional
                alarma = False
                print("Alarma desactivada")

            for i in range(4):
                ingresarCodigo = input(f"Ingregar letra N.ro {i+1}, del codigo: ")
                while not ingresarCodigo.isalpha() or len(ingresarCodigo) != 1:
                  ingresarCodigo = input("Ingresar solo una letra: ")
                codigo_parcial += ingresarCodigo

            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                codigo_parcial = ""
            
        case 3:
            print("Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)")
            forzarCerradura = 0 
            tiempo -= 1
            energia += 15
            
            if energia > 100:
                energia = 100
                
            if alarma == True:
                energia -= 10


 
    if cerraduras_abiertas == 3:
        print("\n========= \nVICTORIA ^-^\n=========")
        inicioJuego = False
    elif energia <= 0 or tiempo <= 0:
        print("======_= \nDERROTA :(\n=========")
        inicioJuego = False
    elif alarma == True and tiempo <= 3:
        print("================== \nDERROTA (bloqueo) :(\n==================")
        inicioJuego = False

    