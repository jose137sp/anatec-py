from random import*

def menu():
    print("\nBienvenido a AnaTec".center(40, " "))
    print("Producto" .ljust(20, " "), "Codigo\n".rjust(20, " "))
    print("Mouse" .ljust(20, "."), "1".rjust(20, "."))
    print("Teclado" .ljust(20, "."), "2".rjust(20, "."))
    print("Cable HDMI" .ljust(20, "."), "3".rjust(20, "."))
    print("Monitor" .ljust(20, "."), "4".rjust(20, "."))
    print("USB" .ljust(20, "."), "5".rjust(20, "."))
    print("Memoria RAM" .ljust(20, "."), "6".rjust(20, "."))
    print("Disco Duro" .ljust(20, "."), "7".rjust(20, "."))
    print("Tarjeta Grafica" .ljust(20, "."), "8".rjust(20, "."))
    print("Cargador" .ljust(20, "."), "9".rjust(20, "."))


subtotal=0
i='1'
while i=='1':
    menu()
    x = int(input("\nIntroduzca el codigo: "))
    if x == 1:
        print("\nEl precio es de: $15.00")
        cant = int(input("¿Qué cantidad va a llevar?: "))
        total = 15.00*cant
    elif x == 2:
        print("\nEl precio es de: $25.00")
        cant = int(input("¿Qué cantidad va a llevar?: "))
        total = 25.00*cant
    elif x == 3:
        print("\nEl precio es de: $17.50")
        cant = int(input("¿Qué cantidad va a llevar?: "))
        total = 17.50*cant
    elif x == 4:
        print("\nEl precio es de: $120.00")
        cant = int(input("¿Qué cantidad va a llevar?: "))
        total = 120.00*cant
    elif x == 5:
        print("El precio es de: $8.00")
        cant = int(input("¿Qué cantidad va a llevar?: "))
        total = 8.00*cant
    elif x == 6:
        print("El precio es de: $30.00")
        cant = int(input("¿Qué cantidad va a llevar?: "))
        total = 30.00*cant
    elif x == 7:
        print("\nEl precio es de: $100.00")
        cant = int(input("¿Qué cantidad va a llevar?: "))
        total = 100.00*cant
    elif x == 8:
        print("\nEl precio es de: $300.00")
        cant = int(input("¿Qué cantidad va a llevar?: "))
        total = 300.00*cant
    elif x == 9:
        print("\nEl precio es de: $25.50")
        cant = int(input("¿Qué cantidad va a llevar?: "))
        total = 25.50*cant

    subtotal=subtotal+total
    print("\nEl total de este producto es: ",total)
    print("\nEl subtotal es: ",subtotal)

    

    i=(input("Introduzca 1 si quiere continuar, de lo contrario presione otra tecla: "))
    print()
else:
    def descuento (num):
        if num == 1:
            desc = 0
        elif num == 2:
            desc = 0.10
        elif num == 3:
            desc = 0.20
        elif num == 3:
            desc = 0.25
        else: desc = 0.50
        return desc

    def color (num):
        if num == 1: color= 'BLANCO'
        elif num == 2: color = 'ROJO'
        elif num == 3: color = 'AZUL'
        elif num == 3: color = 'VERDE'
        else: color = 'AMARILLA'
        return color

    if subtotal >= 100:
        print("  COLOR \t   DESCUENTO" )
        print("BOLA BLANCA\t   NO TIENE")
        print("BOLA ROJA \t 10 POR CIENTO")
        print("BOLA AZUL \t 20 POR CIENTO")
        print("BOLA VERDE \t 25 POR CIENTO")
        print("BOLA AMARILLA \t 50 POR CIENTO")

        bola = randint(1, 5)
        print("\nBOLA #:",bola, "COLOR:",color(bola))
        descuento(bola)
        desc=descuento(bola)*subtotal
        totdesc=subtotal-desc

        print("\nSubtotal: ",subtotal)
        print("Descuento: ", descuento(bola)*100, "%")
        print("Se le desconto: $", desc)
        print("Su total a pagar: $", totdesc)
        
    else: print("NO APLICA EL DESCUENTO, Su total a pagar es: ", subtotal)


