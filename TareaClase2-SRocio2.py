'''
Realizar una calculadora en donde se le pida al usuario una operación
Validar (“+” , “-” , “/”, “*”) en caso de no ser ninguno de esos especificar error
(+) -> Suma
(-) -> Resta
(/) -> Dividir
(*) -> Multiplicar
Luego de tener el operador, pedir dos números y hacer la operación correspondiente.
'''

operador = input("Ingresa una operación (+, -, /, *): ")
operaciones = ['+', '-', '/', '*']
resultado = None

for op in operaciones:
    for i in range(1):
        if op == operador:
            num1 = int(input("Ingresa el primer número: "))
            num2 = int(input("Ingresa el segundo número: "))
            if op == '+':
                resultado = num1 + num2
            elif op == '-':
                resultado = num1 - num2
            elif op == '*':
                resultado = num1 * num2
            elif op == '/':
                if num2 == 0 :
                   resultado = " Error, es una division por cero." 
                else:
                    resultado = num1 / num2
                  
if resultado is not None:
    print(f"El resultado de {num1}{operador}{num2} es: {resultado}")
else:
    print("Error: Operacion no valida.") 