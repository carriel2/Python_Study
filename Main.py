#Melhoria IF ELSE operadores (classe e funcao)
# Lista Variaveis
saldo = None
escolha = 2
escolha_op = 0
compras = [] 
total_compras = 0
final_valor = 0
JUROS = 0.017
subtotal = 0

# Funções
def escolher_categoria():
    escolha_categoria = input("Qual categoria deseja visualizar? ").upper()
    
    while escolha_categoria not in ['HEADSETS', 'MOUSES', 'TECLADOS']:
        escolha_categoria = input("Insira uma categoria válida: HEADSETS, TECLADOS ou MOUSES ").upper()
        
    return escolha_categoria

def produtos_categorias(saldo, subtotal):
    global categoria_escolhida
    
    Lheadsets = ['Astro', 'Razer', 'Logitech']
    
    if categoria_escolhida == 'HEADSETS':
        headsets = input(f"Temos os seguintes headsets disponíveis:{Lheadsets}, qual deseja comprar? ").title()
        
    while headsets not in Lheadsets:
        headsets = input("Insira um headset que esteja disponível. ").title()
        
    return  
        
def calculos (operação, saldo):
    while operação not in ["soma", "subtração", "multiplicação", "divisão", "nenhuma"]:
        operação = (input("Insira uma operação válida "))
    
    if operação	== "nenhuma":
        return (f"Seu número sem alterações é: {saldo}")
    
    valor_inserido = eval(input("Insira um valor: "))
        
    if operação == "soma":
        return saldo + valor_inserido
    elif operação == "subtração":
        return saldo - valor_inserido
    elif operação == "multiplicação":
        return saldo * valor_inserido
    elif operação == "divisão":
        return saldo / valor_inserido
    
#Lista ([]) de Dicionários({})
# lista_produtos = [{
#     "headsets": {
#         "logitech": 299,
#         "razer": 549,
#         "astro": 799,
#     },
    
#     "mouses":{
#         "reddragon": 149,
#         "corsair": 399,
#         "hyperx": 449,
#     },
    
#     "teclados":{
#         "multilaser": 50,
#         "husky": 299,
#         "gamer g": 149,
#     }
# }]

#Bloco de Operações Matemáticas
while True:
    numentrada = input("Insira um número ")
    
    if numentrada.isdigit():
        saldo = (numentrada)
        break
    else:
        print("Insira apenas números ")

operação = input("Digite a operação desejada: (soma, subtração, divisão, multiplicação ou nenhuma) ").lower()
resultado = calculos(operação,saldo)

print(f"Resultado: {resultado}")

print("Bem-vindo à loja PedralhaTEC, escolha entre as categorias disponíveis: HEADSETS - TECLADOS - MOUSES")
    
categoria_escolhida = escolher_categoria()
teste1 = produtos_categorias(saldo, subtotal)














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