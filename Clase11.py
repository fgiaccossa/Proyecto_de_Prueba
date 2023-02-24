import logging

a=int(input("Ingrese el dividendo: "))
b=int(input("ingrese un divisor diferente de cero: "))
while b==0:
    logging.error("****ERROR EL NUMERO INGRESADO ES CERO****")
    b=int(input("ingrese un divisor diferente de cero: "))

def dividir (a, b):
    logging.info("La división se realizó correctamente")
    return a / b 
    
print(f"El resultado de la operación es: {dividir(a, b)}")

    
        
