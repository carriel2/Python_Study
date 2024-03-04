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
num_armazenado = eval((input("Insira um Número ")))
numopd = 0
escolha = 2

#Lista ([]) de Dicionários({})
lista_produtos = [{
    "Headsets": {
        "Logitech": 299,
        "Razer": 549,
        "Astro": 799,
    },
    
    "Mouses":{
        "RedDragon": 149,
        "Corsair": 399,
        "HyperX": 449,
    },
    
    "Teclados":{
        "Multilaser": 50,
        "Husky": 299,
        "Gamer G": 149,
    }
}]

#Bloco de Operações Matemáticas
while escolha < 0 or escolha > 1 :
    escolha = eval(input(f"Deseja Realizar uma operação com este valor? Digite 1 para sim e 0 para não "))

    if escolha < 0 or escolha > 1 :
        print("Número Inválido, insira somente 0 ou 1 ")
        
    elif escolha == 0:
        print(f"Seu número sem alterações é: {num_armazenado}")
        
    elif escolha == 1:
    
        escolha_op = 0
    
        while escolha_op < 1 or escolha_op > 4:
            escolha_op = eval(input(f"Qual operação deseja realizar? Escolha entre Subtração, Soma, Multiplicação e Divisão de 1 a 4: {1 ,2 ,3, 4} "))
            
        if escolha_op <1 or  escolha_op > 4 :
            print("Número Inválido, insira um valor de 1 a 4") 
        
    
        if escolha_op  == 1 :
            val_subt = eval(input("Insira o valor que deseja subtrair: " ))
            res_subt = subt(val_subt, num_armazenado)
            resultados = res_subt
            print(f"Seu valor em reais após subtrar é: {res_subt}")
        
        elif escolha_op == 2 :
            val_soma = eval(input("Insira o valor que deseja somar: "))
            res_soma = soma(val_soma, num_armazenado)
            resultados = res_soma
            print(f"Seu valor em reais após somar é: {res_soma}")
        
        elif escolha_op == 3 :
            val_mult = eval(input("Insira o valor para ser multiplicado: "))
            res_mult = mult(val_mult, num_armazenado)
            resultados = res_mult
            print(f"Seu valor em reais após somar é: {res_mult}")
      
        elif escolha_op == 4 :
            val_div = eval(input("Insira o valor para ser dividido: ")) 
            res_div = div(val_div, num_armazenado)
            resultados = res_div
            print(f"Seu valor em reais após dividir é: {res_div}")
            resultados
            num_armazenado = resultados

num_armazenado

#Bloco de perguntas lojinha
compras = [] 
total_compras = 0
while num_armazenado >= 50: 

    pergunta_1 = input("""Bem vindo a loja PedralhaTEC, as categorias de produto que temos atualmente são as seguinte: HEADSETS -- MOUSES -- TECLADOS\n
    Escolha uma dessas 3 opções digitando o nome da categoria: """)


    if "HEADSETS" == pergunta_1:
        pergunta2 = input(f"Temos os seguintes Headsets disponíveis, selecione qual deseja comprar:{lista_produtos[0]['Headsets']} ")
    
        if "Astro" == pergunta2:
            num_armazenado = subt(num_armazenado, 799)
            print(f"Compra realizada com sucesso! Seu novo saldo é de {num_armazenado}")
            compras.append('Astro - 799')
            total_compras += 799
            
        elif "Logitech" == pergunta2:
            num_armazenado = subt(num_armazenado, 299)
            print(f"Compra realizada com sucesso! Seu novo saldo é de {num_armazenado} ")
            compras.append('Logitech - 299')
            total_compras += 299
            
        elif "Razer" == pergunta2:
            num_armazenado = subt(num_armazenado, 549)
            print(f"Compra realizada com sucesso! Seu novo saldo é de {num_armazenado} ")
            compras.append('Razer - 549')
            total_compras += 549
            
        else:
            print("Insira um produto válido")

    elif "MOUSES" == pergunta_1:
        pergunta2 = input(f"Temos os seguintes Mouses disponíveis, selecione qual deseja comprar: {lista_produtos[0]['Mouses']} ")

        if "RedDragon" == pergunta2:
            num_armazenado = subt(num_armazenado, 149)
            print(f"Compra realizada com sucesso! Seu novo saldo é de {num_armazenado} ")
            compras.append('RedDragon - 149')
            total_compras += 149
        
        elif "Corsair" == pergunta2:
            num_armazenado = subt(num_armazenado, 399)
            print(f"Compra realizada com sucesso! Seu novo saldo é de: {num_armazenado} ")
            compras.append('Corsair - 399')
            total_compras += 399
    
        elif "HyperX" == pergunta2:
            num_armazenado = subt(num_armazenado, 449)
            print(f"Compra realizada com sucesso! Seu novo saldo é de: {num_armazenado} ")
            compras.append('HyperX - 449')
            total_compras += 449
    
        else:
            print("Insira um produto válido")
        
    elif "TECLADOS" == pergunta_1:
        pergunta2 = input(f"Temos os seguintes Teclados disponíveis, selecione qual deseja comprar: {lista_produtos[0]['Teclados']} ")
    
        if "Multilaser" == pergunta2:
            num_armazenado = subt(num_armazenado, 50)
            print(f"Compra realizada com sucesso! Seu novo saldo é de: {num_armazenado}")
            compras.append('Multilaser - 50 reais')
            total_compras += 50

        elif "Husky" == pergunta2:
            num_armazenado = subt(num_armazenado, 299)
            print(f"Compra realizada com sucesso! Seu novo saldo é de: {num_armazenado} ")
            compras.append('Husky - 299 reais')
            total_compras += 299
        
        elif "Gamer G" == pergunta2:
            num_armazenado = subt(num_armazenado, 149)
            print(f"Compra realizada com sucesso! Seu novo saldo é de: {num_armazenado}")
            compras.append('Gamer G - 149')
            total_compras += 149



print(f'Seu carrinho atual é: {compras}\n Com valor total de {total_compras}')

     
    
          


          
          
          


