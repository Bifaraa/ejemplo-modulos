from src.operaciones.restar import * # el * me importas todas las funciones del archivo 
from src.operaciones.sumar import sumar
from src.operaciones.multiplicar import multiplicar

def caculadora () -> None:
    option = int(input('ingrese una opcion'))
    if (option == 1):
        a = int(input('ingrese un numero'))
        b = int(input('ingrese un numero'))
        print(sumar(a,b))
        
    if (option == 2):
        a = int(input('ingrese un numero'))
        b = int(input('ingrese un numero'))
        print(restar(a,b))
    
    if (option==3):
        a = int(input('ingrese un numero'))
        b = int(input('ingrese un numero'))
        print(multiplicar(a,b))
        
    if (option == 4):
        a = int(input('ingrese un numero'))
        b = int(input('ingrese un numero'))
        print(restarNaturales(a,b))
    