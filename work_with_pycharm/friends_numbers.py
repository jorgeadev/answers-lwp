
def introducir_numero(numero):
    """ Solicita un valor entero y lo devuelve. Mientras el valor ingresado no sea entero, vuelve a solicitarlo. """
    while True:
        entero = input("Ingrese el {} número entero: \n".format(numero))
        try:
            number = int(entero)
            return number
        except ValueError:
            print("ATENCIÓN: Debe ingresar un número entero.")

first_number = introducir_numero("primer")
second_number = introducir_numero("segundo")

def suma_divisors(number):
    suma = 0
    for i in range(1, number):
        if (number % i) == 0:
            suma += i
    return suma

if (suma_divisors(first_number) == second_number) & (suma_divisors(second_number) == first_number):
    print("The numbers entered are friends!!!")
else:
    print("The numbers entered are not friends!!!")