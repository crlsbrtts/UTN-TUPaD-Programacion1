nombreCliente = ""
cantProd = ""
intento = 0
desc = 10 # En %
listCompras = ""
suma = 0
sumaDesc = 0
# Se decara dentro del while ya que no se van a cambiar los datos de nombre del cliente y de la cantidad
print("")
while not nombreCliente.isalpha():
    intento += 1
    nombreCliente = input(f"Nombre de cliente: - Intento {intento}: ").strip()
 
while not cantProd.isdigit() or cantProd == "0":
    cantProd = input("Ingresar la cantidad de productos: ")
cantProd = int(cantProd)  

for i in range(cantProd):
    # Se decara afuera del while para cambiar el precio y el descuento
    precio = input(f"\nIngresar el precio del producto {i+1}: ")
    while not precio.isdigit() or precio == "0":
        precio = input(f"Ingreso precio {i+1} equivocado: ")
    
    aplicaDesc = input(f"Tiene descuento del {desc}% (s/n): ")
    while aplicaDesc.lower() != "s" and aplicaDesc.lower() != "n":
        aplicaDesc = input("Intentar de nuevo (s/n): ")
    
    precio = int(precio)
    suma += precio   
    
    if aplicaDesc.lower() == "s":
        sumaDesc += precio * desc/100    
        
    listCompras = listCompras + f"Producto {i + 1} - Precio: {precio}  Descuento (s/n): {aplicaDesc}\n" 

print(f"\nCliente: {nombreCliente}")
print(f"Cantidad de productos: {cantProd}")    
print(f"{listCompras}\n ")   

print(f"Total sin descuentos: ${suma}")
print(f"Total con descuentos: ${(float(suma) - sumaDesc):.2f}")
print(f"Ahorro: ${sumaDesc:.2f}")
print(f"Promedio por producto: ${((float(suma) - sumaDesc) / cantProd):.2f}")



