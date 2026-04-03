vidaGladiador = 100
vidaEnemigo = 100 
pocionesVida = 3 
dañoBase_ataquePesado = 15 
dañoBase_enemigo = 12 
turnoGladiador = True

mensaje_inicio = True

daño = 0

print("\n--- BIENVENIDO A LA ARENA ---\n") 

nombreGladiador = input("Nombre del Gladiador: ")
while not nombreGladiador.isalpha():
    print("Error: Solo se permiten letras.")    
    nombreGladiador = input("Nombre del Gladiador: ")


while vidaGladiador > 0 and vidaEnemigo > 0:
    if mensaje_inicio:
        print("\n=== INICIO DEL COMBATE ===") 
        mensaje_inicio = False
    else:
        print("\n=== NUEVO TURNO ===")

    print(f"{nombreGladiador} (HP: {vidaGladiador}) vs Enemigo (HP: {vidaEnemigo}) | Pociones: {pocionesVida}\n")

           
    print("1. Ataque Pesado \n2. Ráfaga Veloz \n3. Curar")
    
    menuCombate = input("Elige acción: ")
    while not menuCombate.isdigit() or not (0 < int(menuCombate) < 4):
        menuCombate = input("EError: Ingrese un número válido: ")
    menuCombate = int(menuCombate)
    
    match menuCombate:
        case 1:
            if vidaEnemigo < 20:
                daño = dañoBase_ataquePesado * 1.5
            else:
                daño = dañoBase_ataquePesado
            vidaEnemigo -= daño
            print(f"\n¡Atacaste al enemigo por {daño} puntos de daño!\n")
            
            if vidaEnemigo > 0:
                vidaGladiador -= dañoBase_enemigo
                print(f"El enemigo te atacó por {dañoBase_enemigo} puntos de daño!\n")
           
        case 2:
           for i in range(3):
               print("> Golpe conectado por 5 de daño")
               vidaEnemigo -= 5
           
           if vidaEnemigo > 0:
               vidaGladiador -= dañoBase_enemigo
               print(f"El enemigo te atacó por {dañoBase_enemigo} puntos de daño!\n")
               
        case 3:
           if pocionesVida > 0:
               vidaGladiador += 30
               pocionesVida -= 1
           else:
               print("¡No quedan pociones!")
               
           if vidaEnemigo > 0:
               vidaGladiador -= dañoBase_enemigo
               print(f"El enemigo te atacó por {dañoBase_enemigo} puntos de daño!\n")

if vidaGladiador > 0: 
    print(f"\n¡VICTORIA! {nombreGladiador} ha ganado la batalla.") 
        
if vidaGladiador <= 0: 
    print("\nDERROTA. Has caído en combate.")    
