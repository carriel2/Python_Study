# Lista variaveis
saldo = None
compras = []
Lheadsets = ['Astro - 649' 'Razer - 449' 'Logitech -  169']
Lmouses = ['Logitech - 199' ' Hyperx - 249' 'Multilaser - 99']
Lteclados =['Corsair' 'RedDragon' 'Gamer G ']
#Input Main
while True:
    try:
        numentrada = int(input("Insira um número "))
        saldo = numentrada
        break
    except ValueError:
        print("Insira somente números!")

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

#Input de qual operação deseja realizar
operacao = input("Digite a operação desejada: (soma, subtração, divisão, multiplicação ou nenhuma) ").lower()
#chama a função calculos e a atribui a variavel resultado
resultado = calculos(operacao,saldo)
#Printa a variavel resultado q é a solução da def calculos, utilizando os parametros operacao e saldo
print(f"Resultado: {resultado}")

#Ínicio da minha lojinha
print("Bem-vindo à loja PedralhaTEC, escolha entre as categorias disponíveis: HEADSETS - TECLADOS - MOUSES")
#Função de escolha de categoria
def escolher_categoria():

    escolha_categoria = input("Qual categoria deseja visualizar? ").upper()
    
    while escolha_categoria not in ['HEADSETS', 'MOUSES', 'TECLADOS']:
        escolha_categoria = input("Insira uma categoria válida: HEADSETS, TECLADOS ou MOUSES ").upper()
        
    return escolha_categoria

#Função de escolha de produtos dentro da categoria
def produtos_categorias():
    
    if saldo >= 50:
    
        #chamando a função escolher categoria, dentro desta outra função
        if escolher_categoria() == 'HEADSETS':
            headsets = input(f"Temos os seguintes headsets disponíveis:{Lheadsets}, qual deseja comprar? ").title()
            
            while headsets not in Lheadsets:
                headsets = input("Insira um headset que esteja disponível. ").title()
                
            while True:
                try:
                    qtd_headsets = int(input(f"Quantas unidades deseja comprar? "))
                    break
                except ValueError:
                    print("Insira somente números")
                compras.append(headsets * qtd_headsets)
                print(compras)
            
        elif escolher_categoria() == 'MOUSES':
            mouses = input(f"Temos os seguintes mouses disponíveis: {Lmouses}, qual deseja comprar? ").title()
            
            while mouses not in Lmouses:
                mouses = input("Insira um mouse que esteja disponível. ").title()
            
            while True:
                try :
                    qtd_mouses = int(input(f"Quantas unidades deseja comprar: "))
                    break
                except ValueError:
                    print("Insira somente números")
                compras.append(mouses * qtd_mouses)
                print(compras)
                
        elif escolher_categoria() == 'TECLADOS':
            teclados = input(f"Temos os seguintes teclados disponíveis: {Lteclados}, qual deseja comprar? ").title()
            
            while teclados not in Lteclados:
                teclados = input("Insira um teclado que esteja disponível ")
            
            while True:
                try:
                    qtd_teclados = int(input(f"Quantas unidades deseja comprar? "))
                    break
                except ValueError:
                    print("Insira somente números")
                compras.append(teclados * qtd_teclados)
                print(compras)
        
                
        

#Chamando a função produtos_categoria e atribuindo a def a variavel escolha_produto
escolha_produto = produtos_categorias()
print (escolha_produto)
print (compras)


# print('=' * 30)
# print("\tResumo do Pedido")
# print('=' * 30)

# quantidade_total = quantidade_itens_pedido * compras
# print(f"Seu total de itens no pedido é de: {quantidade_itens_pedido}")
# print(f"O total da sua compra é de: {total_compras}")

# print(quantidade_total) 
    
# while final_valor != 0  and final_valor != 1:
#     final_valor = eval(input("Insira uma opção válida "))
    
# if final_valor == 1:
#     num_parcelas = eval(input(f"Em quantas vezes deseja parcelar?Digite de 2 a 6 quantas prestações deseja(Máximo de 6x com juros) "))
#     valor_parcela = (total_compras * (1 + JUROS) ** num_parcelas) / num_parcelas
    
#     if num_parcelas <= 6 :
#         print(f"Sua compra foi parcelada em {num_parcelas}x, com um valor a ser pago por mês de {valor_parcela} ")
    
# elif final_valor == 0:
#     print(f"Já que não deseja parcelar, seu valor total de compra é de {total_compras}")