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
        "Razer": 339,
    }
}]
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
            print(f"Seu valor em reais após subtrar é: {res_subt}")
        
        elif escolha_op == 2 :
            val_soma = eval(input("Insira o valor que deseja somar: "))
            res_soma = soma(val_soma, num_armazenado)
            print(f"Seu valor em reais após somar é: {res_soma}")
        
        elif escolha_op == 3 :
            val_mult = eval(input("Insira o valor para ser multiplicado: "))
            res_mult = mult(val_mult, num_armazenado)
            print(f"Seu valor em reais após somar é: {res_mult}")
      
        elif escolha_op == 4 :
            val_div = eval(input("Insira o valor para ser dividido: ")) 
            res_div = div(val_div, num_armazenado)
            print(f"Seu valor em reais após dividir é: {res_div}")
            
pergunta_1 = input("""Bem vindo a loja PedralhaTEC, as categorias de produto que temos atualmente são as seguinte: HEADSETS -- MOUSES -- TECLADOS\n
Escolha uma dessas 3 opções digitando o nome da categoria: """)   

if "HEADSETS" in pergunta_1:
    print(lista_produtos[0]['Headsets'] )
    a = soma(num1=lista_produtos[0]['Headsets']['Logitech'], num2=lista_produtos[0]["Teclados"]['Multilaser'])
    print(a)


# ListaProdutos = [{
#     "Headsets": {
#         "Logitech": 299,
#         "Razer": 549,
#         "Astro": 799,
#     },
    
#     "Mouses":{
#         "RedDragon": 149,
#         "Corsair": 399,
#         "HyperX": 449,
#     },
    
#     "Teclados":{
#         "Multilaser": 50,
#         "Husky": 299,
#         "Razer": 339,
#     }
# }]
     
    
          




          
          
          


