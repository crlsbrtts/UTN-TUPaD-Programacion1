
accesoTurno = True
turnoLunes = 4
turnoMartes = 3
nombrePaciente = ""
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""



while accesoTurno:
    print("\n----------------------------\nAgenda de Turnos con Nombres\n------ -- ------ --- -------\n" \
    "1. Reservar turno\n" \
    "2. Cancelar turno (por nombre)\n" \
    "3. Ver agenda del día\n" \
    "4. Ver resumen general\n" \
    "5. Cerrar sistema\n----------------------------")
    menuTurnos = input("Opcion: ")
    while not menuTurnos.isdigit() or not(0 < int(menuTurnos) < 6) or len(menuTurnos) > 1:
        menuTurnos = input("Numero equivocado, ingrese nuevamente el N.ro: ")
    
    menuTurnos = int(menuTurnos)
    
    match menuTurnos:
        case 1:
            print(f"\nReservar turno\nTurnos:\nLunes   - {turnoLunes} turnos disponibles\nMartes  - {turnoMartes} turnos disponibles")
            
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
            while not(dia == "1") and not(dia == "2"):
                dia = input("Intentar otra vez (1=Lunes, 2=Martes): ")
            dia = int(dia)

            if (dia == 1 and turnoLunes == 0) or (dia == 2 and turnoMartes == 0):
                print("No hay turnos disponibles")
                
            else:
                nombrePaciente = input("Nombre del paciente (solo letras): ")
                while not nombrePaciente.isalpha():
                    nombrePaciente = input("Solo letras: ")
                nombrePaciente = nombrePaciente.lower()
                
                if dia == 1 and turnoLunes > 0:                
                    if lunes1 == "":
                        lunes1 = nombrePaciente
                        turnoLunes -= 1
                        print(f"Turno Lunes, N.ro 1")  
                    elif lunes2 == "":
                        lunes2 = nombrePaciente
                        turnoLunes -= 1
                        print(f"Turno Lunes, N.ro 2")     
                    elif lunes3 == "":
                        lunes3 = nombrePaciente
                        turnoLunes -= 1
                        print(f"Turno Lunes, N.ro 3")  
                    elif lunes4 == "":
                        lunes4 = nombrePaciente
                        turnoLunes -= 1
                        print(f"Turno Lunes, N.ro 4")  
                    else:
                        print(f"Turno: {turnoLunes} el día {dia}: - No disponible.")    
        
                

                elif dia == 2 and turnoMartes > 0:    
                    if martes1 == "":
                        martes1 = nombrePaciente
                        print(f"Turno Martes, N.ro 1")
                        turnoMartes -= 1    
                    elif martes2 == "":
                        martes2 = nombrePaciente
                        print(f"Turno Martes, N.ro 2")
                        turnoMartes -= 1  
                    elif martes3 == "":
                        martes3 = nombrePaciente 
                        print(f"Turno Martes, N.ro 3")
                        turnoMartes -= 1  
                    else:
                        print(f"Turno: {turnoMartes} el día {dia}: - No disponible.") 
                    

        
        case 2:
            print("----------------\nCancelar turno\n----------------\n")

            dia = input("Elegir día (1=Lunes, 2=Martes): ")
            while not(dia == "1") and not(dia == "2"):
                dia = input("Intentar otra vez (1=Lunes, 2=Martes): ")
            dia = int(dia)
            
            nombrePaciente = input("Nombre del paciente (solo letras): ")
            while not nombrePaciente.isalpha():
                nombrePaciente = input("Solo letras: ")
            nombrePaciente = nombrePaciente.lower().strip()

            encontrado = False
            
            if dia == 1:                
                
                if lunes1.lower() == nombrePaciente:
                    lunes1 = ""
                    turnoLunes += 1
                    encontrado = True
                    print(f"Turno Lunes, N.ro 1")  
                elif lunes2.lower() == nombrePaciente:
                    lunes2 = ""
                    turnoLunes += 1
                    encontrado = True
                    print(f"Turno Lunes, N.ro 2")     
                elif lunes3.lower() == nombrePaciente:
                    lunes3 = ""
                    turnoLunes += 1
                    encontrado = True
                    print(f"Turno Lunes, N.ro 3")  
                elif lunes4.lower() == nombrePaciente:
                    lunes4 = ""
                    turnoLunes += 1
                    encontrado = True
                    print(f"Turno Lunes, N.ro 4")
                

            elif dia == 2:    
             
                if martes1.lower() == nombrePaciente:
                    martes1 = ""
                    turnoMartes += 1
                    encontrado = True
                    print(f"Turno Martes, N.ro 1")    
                elif martes2.lower() == nombrePaciente:
                    martes2 = ""
                    turnoMartes += 1
                    encontrado = True
                    print(f"Turno Martes, N.ro 2")  
                elif martes3.lower() == nombrePaciente:
                    martes3 = ""
                    turnoMartes += 1
                    encontrado = True
                    print(f"Turno Martes, N.ro 3")  
                
            if encontrado:
                print("Paciente encontrado")
            else:
                print("Paciente NO encontrado")
            
        case 3:
            
            print("----------------\nAgenda del día:\n----------------")
    
            print("\nLunes\n------")
            contTurno = 0
            if lunes1 == "":
                contTurno += 1
                print(f"Turno {contTurno}: Libre")
            else:
                contTurno += 1
                print(f"Turno {contTurno}: {lunes1.capitalize()}")    
            if lunes2 == "":
                contTurno += 1
                print(f"Turno {contTurno}: Libre")
            else:
                contTurno += 1
                print(f"Turno {contTurno}: {lunes2.capitalize()}")   
            if lunes3 == "":
                contTurno += 1
                print(f"Turno {contTurno}: Libre")
            else:
                contTurno += 1
                print(f"Turno {contTurno}: {lunes3.capitalize()}")
            if lunes4 == "":
                contTurno += 1
                print(f"Turno {contTurno}: Libre")
            else:
                contTurno += 1
                print(f"Turno {contTurno}: {lunes4.capitalize()}")
            
            contTurno = 0
            print("\nMartes\n------")
            if martes1 == "":
                contTurno += 1
                print(f"Turno {contTurno}: Libre")
            else:
                contTurno += 1
                print(f"Turno {contTurno}: {martes1.capitalize()}") 
            if martes2 == "":
                contTurno += 1
                print(f"Turno {contTurno}: Libre")
            else:
                contTurno += 1
                print(f"Turno {contTurno}: {martes2.capitalize()}")
            if martes3 == "":
                contTurno += 1
                print(f"Turno {contTurno}: Libre")
            else:
                contTurno += 1
                print(f"Turno {contTurno}: {martes3.capitalize()}")
        
        
        case 4:
            
            print(f"Lunes   - {turnoLunes} turno/s disponible/s - {4 - turnoLunes} turno/s ocupado/s \nMartes  - {turnoMartes} turno/s disponible/s - {3 - turnoMartes} turno/s ocupado/s ")
            
            if turnoLunes > turnoMartes:
                print(f"Lunes: {turnoLunes - turnoMartes} más")
            elif turnoLunes < turnoMartes:
                print(f"Martes: {turnoMartes - turnoLunes} más")
            elif turnoLunes == 0 and turnoMartes == 0:
                print("Sin turnos disponiobles")
            else:    
                print(f"Lunes: {turnoLunes} y Martes: {turnoMartes} - Empate")
               
        
            
        case 5:    

            print("Salir")
            accesoTurno = False
