# Lista variaveis
saldo = None
Lheadsets = ['Astro', 'Razer', 'Logitech']
Lmouses = ['Logitech', 'Hyperx', 'Multilaser']
Lteclados =['Corsair', 'Reddragon', 'Gamer G']

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
            if valor_inserido == 0:
                return "ERRO: Divisão por 0 não é permitida."
            else:
                return saldo / (valor_inserido)

#Função de escolha de categoria
def escolher_categoria():

    escolha_categoria = input("Qual categoria deseja visualizar? ").upper()
    
    while escolha_categoria not in ['HEADSETS', 'MOUSES', 'TECLADOS']:
        escolha_categoria = input("Insira uma categoria válida: HEADSETS, TECLADOS ou MOUSES ").upper()
        
    return escolha_categoria

#Função de escolha de produtos dentro da categoria
def produtos_categorias(saldo):
    carrinho = []

    while True:
        print("Bem-vindo à loja PedralhaTEC, escolha entre as categorias disponíveis: HEADSETS - TECLADOS - MOUSES")
        escolha_categoria = input("Digite a categoria desejada ou 'Sair' para finalizar a compra: ").upper()
        
        if escolha_categoria == 'SAIR':
            break
        
        if saldo >= 50:
            if escolha_categoria == 'HEADSETS':
                while True:
                    headsets = input(f"Temos os seguintes headsets disponíveis: {Lheadsets}, qual deseja comprar? ").title()
                    
                    if headsets in Lheadsets:
                        while True:
                            try:
                                qtd_headsets = int(input(f"Quantas unidades deseja comprar? "))
                                carrinho.append(f'Categoria - Headset: {headsets} || Quantidade de produtos: {qtd_headsets}')
                                continuar = input("Deseja continuar comprando headsets? (Sim/Não) ").title()
                                if continuar != 'Sim':
                                    break
                                else:
                                    break
                            except ValueError:
                                print("Insira somente números")
                        break
                    else:
                        print("Insira um headset que esteja disponível.")
            
            elif escolha_categoria == 'MOUSES':
                while True:
                    mouses = input(f"Temos os seguintes mouses disponíveis: {Lmouses}, qual deseja comprar? ").title()
                    
                    if mouses in Lmouses:
                        while True:
                            try:
                                qtd_mouses = int(input(f"Quantas unidades deseja comprar: "))
                                carrinho.append(f'Categoria - Mouse: {mouses} || Quantidade de produtos: {qtd_mouses}')
                                continuar = input("Deseja continuar comprando mouses? (Sim/Não) ").title()
                                if continuar != 'Sim':
                                    break
                                else:
                                    break
                            except ValueError:
                                print("Insira somente números")
                        break
                    else:
                        print("Insira um mouse que esteja disponível.")
            
            elif escolha_categoria == 'TECLADOS':
                while True:
                    teclados = input(f"Temos os seguintes teclados disponíveis: {Lteclados}, qual deseja comprar? ").title()
                    
                    if teclados in Lteclados:
                        while True:
                            try:
                                qtd_teclados = int(input(f"Quantas unidades deseja comprar? "))
                                carrinho.append(f'Categoria - Teclado: {teclados} || Quantidade de produtos: {qtd_teclados}')
                                continuar = input("Deseja continuar comprando teclados? (Sim/Não) ").title()
                                if continuar != 'Sim':
                                    break
                                else:
                                    break
                            except ValueError:
                                print("Insira somente números")
                        break
                    else:
                        print("Insira um teclado que esteja disponível.")
        else:
            print("Seu saldo não é suficiente para comprar nenhum produto da loja")

    print("Produtos no carrinho:")
    for produto in carrinho:
        print(produto)

    
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

#Chamando a função produtos_categoria e atribuindo a def a variavel escolha_produto
escolha_produto = produtos_categorias(saldo)


