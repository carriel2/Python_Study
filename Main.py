#Melhoria IF ELSE operadores (classe e funcao)
# Lista Variaveis
num_armazenado = 'A'
escolha = 2
escolha_op = 0
compras = [] 
total_compras = 0
final_valor = 0
JUROS = 0.017

# Funções

def calculos (operação, num_armazenado):
    while operação not in ["soma", "subtração", "multiplicação", "divisão", "nenhuma"]:
        (input("Insira uma operação válida "))
    
    valor_inserido = eval(input("Insira um valor: "))
        
    if operação == "soma":
        return num_armazenado + valor_inserido
    elif operação == "subtração":
        return num_armazenado - valor_inserido
    elif operação == "multiplicação":
        return num_armazenado * valor_inserido
    elif operação == "divisão":
        return num_armazenado / valor_inserido
    elif operação == "nenhuma":
        return (f"Seu número sem alterações é: {num_armazenado}")
    

# def subtração ():
#     val_subt = eval(input("Insira um valor para ser subtraído "))
#     total_subt = num_armazenado - val_subt
#     return total_subt

# def soma ():
#     val_soma = eval(input("Insira um valor para ser somado "))
#     total_soma = num_armazenado + val_soma
#     return total_soma

# def multiplicação ():
#     val_mult = eval(input("Insira um valor para ser multiplicado "))
#     total_mult = num_armazenado * val_mult
#     return total_mult


# def divisão ():
#     val_div = eval(input("Insira um valor para ser dividido "))
#     total_div = num_armazenado / val_div
#     return total_div

#Lista ([]) de Dicionários({})
lista_produtos = [{
    "Headsets": {
        "LOGITECH": 299,
        "RAZER": 549,
        "ASTRO": 799,
    },
    
    "Mouses":{
        "REDDRAGON": 149,
        "CORSAIR": 399,
        "HYPERX": 449,
    },
    
    "Teclados":{
        "MULTILASER": 50,
        "HUSKY": 299,
        "GAMER G": 149,
    }
}]

#Bloco de Operações Matemáticas
num_armazenado = eval((input("Insira um Número ")))

operação = input("Digite a operação desejada: (soma, subtração, divisão, multiplicação ou nenhuma) ").lower()
resultado = calculos(operação,num_armazenado)

print(f"Resultado: {resultado}")

#Bloco de perguntas lojinha
while num_armazenado >= 50: 

    pergunta_1 = input("""Bem vindo a loja PedralhaTEC, as categorias de produto que temos atualmente são as seguinte: HEADSETS -- MOUSES -- TECLADOS\n
    Escolha uma dessas 3 opções digitando o nome da categoria: """).upper()
    
    if "HEADSETS" == pergunta_1:
        pergunta2 = input(f"Temos os seguintes Headsets disponíveis, selecione qual deseja comprar:{lista_produtos[0]['Headsets']} ").upper()
    
        if "ASTRO" == pergunta2:
            quantidade_itens_pedido = int(input("Digite a quantidade que deseja comprar: "))
            num_armazenado -= 799 * quantidade_itens_pedido
            print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de {num_armazenado} ")
            compras.append('Astro - 799')
            total_compras += 799 * quantidade_itens_pedido
            
        elif "LOGITECH" == pergunta2:
            quantidade_itens_pedido = int(input("Digite a quantidade que deseja comprar: "))
            num_armazenado -= 299 * quantidade_itens_pedido
            print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de {num_armazenado} ")
            compras.append('Logitech - 299')
            total_compras += 299 * quantidade_itens_pedido
            
        elif "RAZER" == pergunta2:
            quantidade_itens_pedido = int(input)("Digite a quantidade que deseja comprar: ")
            num_armazenado -= 549 * quantidade_itens_pedido
            print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de {num_armazenado} ")
            compras.append('Razer - 549')
            total_compras += 549 * quantidade_itens_pedido
            
        else:
            print("Insira um produto válido")

    elif "MOUSES" == pergunta_1:
        pergunta2 = input(f"Temos os seguintes Mouses disponíveis, selecione qual deseja comprar: {lista_produtos[0]['Mouses']} ").upper()

        if "REDDRAGON" == pergunta2:
            quantidade_itens_pedido = int(input("Digite a quantidade que deseja comprar: "))
            num_armazenado -= 149 * quantidade_itens_pedido
            print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de {num_armazenado} ")
            compras.append('RedDragon - 149')
            total_compras += 149 * quantidade_itens_pedido
        
        elif "CORSAIR" == pergunta2:
            quantidade_itens_pedido = int(input("Digite a quantidade que deseja comprar: "))
            num_armazenado -= 399 * quantidade_itens_pedido
            print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de {num_armazenado} ")
            compras.append('Corsair - 399')
            total_compras += 399 * quantidade_itens_pedido
    
        elif "HYPERX" == pergunta2:
            num_armazenado = int(input("Digite a quantidade que deseja comprar: "))
            num_armazenado -= 149 * quantidade_itens_pedido
            print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de: {num_armazenado} ")
            compras.append('HyperX - 449')
            total_compras += 449 * quantidade_itens_pedido
    
        else:
            print("Insira um produto válido")
        
    elif "TECLADOS" == pergunta_1:
        pergunta2 = input(f"Temos os seguintes Teclados disponíveis, selecione qual deseja comprar: {lista_produtos[0]['Teclados']} ").upper()
    
        if "MULTILASER" == pergunta2:
            num_armazenado = int(input("Digite a quantidade que deseja comprar: "))
            num_armazenado -= 50 * quantidade_itens_pedido
            print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de: {num_armazenado}")
            compras.append('Multilaser - 50 reais')
            total_compras += 50 * quantidade_itens_pedido

        elif "HUSKY" == pergunta2:
            num_armazenado = int(input("Digite a quantidade que deseja comprar: "))
            num_armazenado -= 299 * quantidade_itens_pedido
            print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de: {num_armazenado} ")
            compras.append('Husky - 299 reais')
            total_compras += 299 * quantidade_itens_pedido
        
        elif "GAMER G" == pergunta2:
            num_armazenado = int(input("Digite a quantidade que deseja comprar: "))
            num_armazenado -= 149 * quantidade_itens_pedido
            print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de: {num_armazenado}")
            compras.append('Gamer G - 149')
            total_compras += 149 * quantidade_itens_pedido
        
        else:
            print("Insira um produto válido")
            
print('=' * 30)
print("\tResumo do Pedido")
print('=' * 30)

quantidade_total = quantidade_itens_pedido * compras
print(f"Seu total de itens no pedido é de: {quantidade_itens_pedido}")
print(f"O total da sua compra é de: {total_compras}")

print(quantidade_total) 
    
while final_valor != 0  and final_valor != 1:
    final_valor = eval(input("Insira uma opção válida "))
    
if final_valor == 1:
    num_parcelas = eval(input(f"Em quantas vezes deseja parcelar?Digite de 2 a 6 quantas prestações deseja(Máximo de 6x com juros) "))
    valor_parcela = (total_compras * (1 + JUROS) ** num_parcelas) / num_parcelas
    
    if num_parcelas <= 6 :
        print(f"Sua compra foi parcelada em {num_parcelas}x, com um valor a ser pago por mês de {valor_parcela} ")
    
elif final_valor == 0:
    print(f"Já que não deseja parcelar, seu valor total de compra é de {total_compras}")