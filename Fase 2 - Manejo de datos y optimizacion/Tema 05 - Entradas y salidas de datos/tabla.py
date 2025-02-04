import sys
if len(sys.argv) ==3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    
    if filas > 1 and filas < 10: 
        print("El primer número esta dentro de rango del 1 al 10")
        if columnas > 1 and columnas < 10:
                print("El segundo número esta dentro de rango del 1 al 10")
                for f in range (filas):
                    for c in range (columnas):
                        print("*", end ='')
        else: 
            print("Error, Las columnas deben ir de 1 a 9 ")
    else: 
        print:("Error, ambos números deben estar entre el 1 y el 9")
else:
    print("Error, solo se permite ingresar 2 números del 1 al 9, por ejemplo 2_3")
