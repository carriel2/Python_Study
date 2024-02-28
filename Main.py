num_armazenado = eval((input("Insira um Número ")))
numop = 0
sim = 1
não = 0
escolha = 2

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
            val_Sub = eval(input(f"Insira o valor que deseja subtrair do total: " ))
            res_Sub = num_armazenado - val_Sub
            print(f"Seu numero subtraido é: {res_Sub}")
        
        elif escolha_op == 2 :
            val_Soma = eval(input(f"Insira o valor a ser somado: "))
            res_Soma = num_armazenado + val_Soma
            print(f"Seu número já somado é: {res_Soma}")
        
        elif escolha_op == 3 :
            val_Mult = eval(input(f"Insira o valor para ser multiplicado: "))
            res_Mult = num_armazenado * val_Mult
            print(f"Seu valor multiplicado é: {res_Mult}")
      
        elif escolha_op == 4 :
            val_Div = eval(input(f"Insira o valor para ser dividido: ")) 
            res_Div = num_armazenado / val_Div
            print(f"Seu valor dividido é: {res_Div}")
