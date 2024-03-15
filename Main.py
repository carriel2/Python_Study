# Lista variaveis
saldo = None
compras = []
Lheadsets = ['Astro', 'Razer', 'Logitech']
Lmouses = ['Logitech', 'Hyperx', 'Multilaser']
Lteclados =['Corsair', 'RedDragon', 'Gamer G']

#Função cálculos
def calculos (operacao, saldo):
    while operacao not in ["soma", "subtração", "multiplicação", "divisão", "nenhuma"]:
        operacao = (input("Insira uma operação válida "))
    
    if operacao	== "nenhuma":
        return (f"Seu número sem alterações é: {saldo}")
    
    while True:
        try:
            valor_inserido = int(input("Insira um valor: "))
            break
        except ValueError:
            print("Insira somente números!")
    
    if operacao == "soma":
        return saldo + (valor_inserido)
    elif operacao == "subtração":
        return saldo - (valor_inserido)
    elif operacao == "multiplicação":
        return saldo * (valor_inserido)
    elif operacao == "divisão":
        return saldo / (valor_inserido)

#Função de escolha de categoria
def escolher_categoria():

    escolha_categoria = input("Qual categoria deseja visualizar? ").upper()
    
    while escolha_categoria not in ['HEADSETS', 'MOUSES', 'TECLADOS']:
        escolha_categoria = input("Insira uma categoria válida: HEADSETS, TECLADOS ou MOUSES ").upper()
        
    return escolha_categoria

#Função de escolha de produtos dentro da categoria
def produtos_categorias():
    escolha_categoria = escolher_categoria()
    if saldo >= 50:
    
        #chamando a função escolher categoria, dentro desta outra função
        if escolha_categoria == 'HEADSETS':
            headsets = input(f"Temos os seguintes headsets disponíveis:{Lheadsets}, qual deseja comprar? ").title()
            
            while headsets not in Lheadsets:
                headsets = input("Insira um headset que esteja disponível. ").title()
                
            while True:
                try:
                    qtd_headsets = int(input(f"Quantas unidades deseja comprar? "))
                    compras.append(headsets * qtd_headsets)
                    break
                except ValueError:
                    print("Insira somente números")
            
        elif escolha_categoria == 'MOUSES':
            mouses = input(f"Temos os seguintes mouses disponíveis: {Lmouses}, qual deseja comprar? ").title()
            
            while mouses not in Lmouses:
                mouses = input("Insira um mouse que esteja disponível. ").title()
            
            while True:
                try :
                    qtd_mouses = int(input(f"Quantas unidades deseja comprar: "))
                    teste = (f'{mouses} * {qtd_mouses}')
                    compras.append (teste)
                    
                    break
                except ValueError:
                    print("Insira somente números")
                
        elif escolha_categoria == 'TECLADOS':
            teclados = input(f"Temos os seguintes teclados disponíveis: {Lteclados}, qual deseja comprar? ").title()
            
            while teclados not in Lteclados:
                teclados = input("Insira um teclado que esteja disponível ")
            
            while True:
                try:
                    qtd_teclados = int(input(f"Quantas unidades deseja comprar? "))
                    compras.append(teclados * qtd_teclados)
                    break
                except ValueError:
                    print("Insira somente números")
    else:
        print("Seu saldo não é suficiente para comprar nenhum produto da loja")
    
while True:
    try:
        numentrada = int(input("Insira um número "))
        saldo = numentrada
        break
    except ValueError:
        print("Insira somente números!")
        
#Input de qual operação deseja realizar
operacao = input("Digite a operação desejada: (soma, subtração, divisão, multiplicação ou nenhuma) ").lower()

#chama a função calculos e a atribui a variavel resultado
resultado = calculos(operacao,saldo)

#Printa a variavel resultado q é a solução da def calculos, utilizando os parametros operacao e saldo
print(f"Saldo total: {resultado}")

#Ínicio da minha lojinha
print("Bem-vindo à loja PedralhaTEC, escolha entre as categorias disponíveis: HEADSETS - TECLADOS - MOUSES")

#Chamando a função produtos_categoria e atribuindo a def a variavel escolha_produto
escolha_produto = produtos_categorias()

print(compras)


