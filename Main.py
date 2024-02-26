num_armazenado = (input("Insira um Número "))
numop = 0
sim = 1
não = 0
AM = eval(num_armazenado)


escolha = eval(input(f"Deseja Realizar uma operação com este valor? Digite 1 para sim e 0 para não "))

if escolha == 1 :
    escolha_op = eval(input(f"Qual operação deseja realizar? Escolha entre Subtração, Soma, Multiplicação e Divisão de 1 a 4: {1 ,2 ,3, 4} "))
    
    if escolha_op  == 1 :
        val_Sub = eval(input(f"Insira o valor que deseja subtrair do total: " ))
        res_Sub = AM - val_Sub
        print(f"Seu numero subtraido é: {res_Sub}")
        
    elif escolha_op == 2 :
        val_Soma = eval(input(f"Insira o valor a ser somado: "))
        res_Soma = AM + val_Soma
        print(f"Seu número já somado é: {res_Soma}")
        
    elif escolha_op == 3 :
        val_Mult = eval(input(f"Insira o valor para ser multiplicado: "))
        res_Mult = AM * val_Mult
        print(f"Seu valor multiplicado é: {res_Mult}")
        
    else :
        val_Div = eval(input(f"Insira o valor para ser dividido: ")) 
        res_Div = AM / val_Div
        print(f"Seu valor dividido é: {res_Div}")

else : 
    print(f"Seu número sem alterações é: {AM}")

