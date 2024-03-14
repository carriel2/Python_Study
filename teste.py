# while num_armazenado >= 50: 

#     pergunta_1 = input("""Bem vindo a loja PedralhaTEC, as categorias de produto que temos atualmente são as seguinte: HEADSETS -- MOUSES -- TECLADOS\n
#     Escolha uma dessas 3 opções digitando o nome da categoria: """).upper()
    
#     if "HEADSETS" == pergunta_1:
#         pergunta2 = input(f"Temos os seguintes Headsets disponíveis, selecione qual deseja comprar:{lista_produtos[0]['Headsets']} ").upper()
    
#         if "ASTRO" == pergunta2:
#             quantidade_itens_pedido = int(input("Digite a quantidade que deseja comprar: "))
#             num_armazenado -= 799 * quantidade_itens_pedido
#             print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de {num_armazenado} ")
#             compras.append('Astro - 799')
#             total_compras += 799 * quantidade_itens_pedido
            
#         elif "LOGITECH" == pergunta2:
#             quantidade_itens_pedido = int(input("Digite a quantidade que deseja comprar: "))
#             num_armazenado -= 299 * quantidade_itens_pedido
#             print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de {num_armazenado} ")
#             compras.append('Logitech - 299')
#             total_compras += 299 * quantidade_itens_pedido
            
#         elif "RAZER" == pergunta2:
#             quantidade_itens_pedido = int(input("Digite a quantidade que deseja comprar: "))
#             num_armazenado -= 549 * quantidade_itens_pedido
#             print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de {num_armazenado} ")
#             compras.append('Razer - 549')
#             total_compras += 549 * quantidade_itens_pedido
            
#         else:
#             print("Insira um produto válido")

#     elif "MOUSES" == pergunta_1:
#         pergunta2 = input(f"Temos os seguintes Mouses disponíveis, selecione qual deseja comprar: {lista_produtos[0]['Mouses']} ").upper()

#         if "REDDRAGON" == pergunta2:
#             quantidade_itens_pedido = int(input("Digite a quantidade que deseja comprar: "))
#             num_armazenado -= 149 * quantidade_itens_pedido
#             print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de {num_armazenado} ")
#             compras.append('RedDragon - 149')
#             total_compras += 149 * quantidade_itens_pedido
        
#         elif "CORSAIR" == pergunta2:
#             quantidade_itens_pedido = int(input("Digite a quantidade que deseja comprar: "))
#             num_armazenado -= 399 * quantidade_itens_pedido
#             print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de {num_armazenado} ")
#             compras.append('Corsair - 399')
#             total_compras += 399 * quantidade_itens_pedido
#             if num_armazenado < total_compras:
                
                
#         elif "HYPERX" == pergunta2:
#             num_armazenado = int(input("Digite a quantidade que deseja comprar: "))
#             num_armazenado -= 149 * quantidade_itens_pedido
#             print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de: {num_armazenado} ")
#             compras.append('HyperX - 449')
#             total_compras += 449 * quantidade_itens_pedido
    
#         else:
#             print("Insira um produto válido")
        
#     elif "TECLADOS" == pergunta_1:
#         pergunta2 = input(f"Temos os seguintes Teclados disponíveis, selecione qual deseja comprar: {lista_produtos[0]['Teclados']} ").upper()
    
#         if "MULTILASER" == pergunta2:
#             num_armazenado = int(input("Digite a quantidade que deseja comprar: "))
#             num_armazenado -= 50 * quantidade_itens_pedido
#             print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de: {num_armazenado}")
#             compras.append('Multilaser - 50 reais')
#             total_compras += 50 * quantidade_itens_pedido

#         elif "HUSKY" == pergunta2:
#             num_armazenado = int(input("Digite a quantidade que deseja comprar: "))
#             num_armazenado -= 299 * quantidade_itens_pedido
#             print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de: {num_armazenado} ")
#             compras.append('Husky - 299 reais')
#             total_compras += 299 * quantidade_itens_pedido
        
#         elif "GAMER G" == pergunta2:
#             num_armazenado = int(input("Digite a quantidade que deseja comprar: "))
#             num_armazenado -= 149 * quantidade_itens_pedido
#             print(f"Compra realizada com sucesso! Você comprou {quantidade_itens_pedido} unidades! Seu novo saldo é de: {num_armazenado}")
#             compras.append('Gamer G - 149')
#             total_compras += 149 * quantidade_itens_pedido
        
#         else:
#             print("Insira um produto válido")
            
            
# def soma (num1, num2):
#     resultado = num1 + num2
#     print('pedralha intruso 1')
#     return resultado

# def soma2 (num1, num2):
#     print('pedralha intruso 2')
#     return num1 + num2

# def soma3(a, b):
#     print('pedralha intruso 3')
#     return a+b



# print(f'soma {soma(2,2)}')

# print(f'soma2 {soma2(2,2)}')

# print(f'soma3 {soma3(2,2)}')

# def divideSoma(num1, num2):
#     resultado = soma(num1, num2)
#     resulado_dividido = resultado / 2
#     return resulado_dividido

dict = {'a':1, 'b':2 , 'c':3}

chave = 'a'

# for chave in dict:
print(f'Chave: {chave}, Valor: {dict[chave]}')
print(f'Chave: {}')

