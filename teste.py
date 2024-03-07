def soma (num1, num2):
    resultado = num1 + num2
    print('pedralha intruso 1')
    return resultado

def soma2 (num1, num2):
    print('pedralha intruso 2')
    return num1 + num2

def soma3(a, b):
    print('pedralha intruso 3')
    return a+b



print(f'soma {soma(2,2)}')

print(f'soma2 {soma2(2,2)}')

print(f'soma3 {soma3(2,2)}')

def divideSoma(num1, num2):
    resultado = soma(num1, num2)
    resulado_dividido = resultado / 2
    return resulado_dividido

