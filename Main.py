# Funções
def soma (num1, num2):
    resultado = num1 + num2
    return resultado

def subt (num1, num2):
    resultado = num1 - num2
    return resultado

def mult (num1, num2):
    resultado = num1 * num2
    return resultado

def div (num1, num2):
    resultado = num1 / num2
    return resultado

# Lista Variaveis
num_armazenado = 'A'
escolha = 2
escolha_op = 0
compras = [] 
total_compras = 0
final_valor = 0
JUROS = 0.017

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

num_armazenado = eval((input("Insira um Número ")))

#Bloco de Operações Matemáticas
while escolha < 0 or escolha > 1 :
    escolha = eval(input(f"Deseja Realizar uma operação com este valor? Digite 1 para sim e 0 para não "))

    if escolha < 0 or escolha > 1 :
        print("Número Inválido, insira somente 0 ou 1 ")
        
    elif escolha == 0:
        print(f"Seu número sem alterações é: {num_armazenado}")
        
    elif escolha == 1:
    
        while escolha_op < 1 or escolha_op > 4:
            escolha_op = eval(input(f"Qual operação deseja realizar? Escolha entre Subtração, Soma, Multiplicação e Divisão de 1 a 4: {1 ,2 ,3, 4} "))
            
        if escolha_op <1 or  escolha_op > 4 :
            print("Número Inválido, insira um valor de 1 a 4") 
        
    
        if escolha_op  == 1 :
            val_subt = eval(input("Insira o valor que deseja subtrair: " ))
            res_subt = subt(val_subt, num_armazenado)
            resultados = res_subt
            print(f"Seu valor em reais após subtrair é: {res_subt}")
        
        elif escolha_op == 2 :
            val_soma = eval(input("Insira o valor que deseja somar: "))
            res_soma = soma(val_soma, num_armazenado)
            resultados = res_soma
            print(f"Seu valor em reais após somar é: {res_soma}")
        
        elif escolha_op == 3 :
            val_mult = eval(input("Insira o valor para ser multiplicado: "))
            res_mult = mult(val_mult, num_armazenado)
            resultados = res_mult
            print(f"Seu valor em reais após multiplicar é: {res_mult}")
      
        elif escolha_op == 4 :
            val_div = eval(input("Insira o valor para ser dividido: ")) 
            res_div = div(val_div, num_armazenado)
            resultados = res_div
            print(f"Seu valor em reais após dividir é: {res_div}")
            resultados
            num_armazenado = resultados

num_armazenado

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
    
final_valor = eval(input(f'Seu carrinho atual é: {quantidade_itens_pedido} unidades de {compras}\n Com valor total de {total_compras}, deseja parcelar em até 6x com juros? digite 1 para sim e 0 para não. '))

while final_valor != 0  and final_valor != 1:
    final_valor = eval(input("Insira uma opção válida "))
    
if final_valor == 1:
    num_parcelas = eval(input(f"Em quantas vezes deseja parcelar?Digite de 2 a 6 quantas prestações deseja(Máximo de 6x com juros) "))
    valor_parcela = (total_compras * (1 + JUROS) ** num_parcelas) / num_parcelas
    
    if num_parcelas <= 6 :
        print(f"Sua compra foi parcelada em {num_parcelas}x, com um valor a ser pago por mês de {valor_parcela} ")
    
elif final_valor == 0:
    print(f"Já que não deseja parcelar, seu valor total de compra é de {total_compras}")