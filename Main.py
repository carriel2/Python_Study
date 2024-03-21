headsets = {
    "Astro": 500,
    "Razer": 400,
    "Logitech": 300,
}

mouses = {
    "Logitech": 200,
    "Hyperx": 150,
    "Multilaser": 100,
}

teclados = {
    "Corsair": 600,
    "Reddragon": 450,
    "Gamer G": 350,
}

categorias = {
    "HEADSETS": headsets,
    "MOUSES": mouses,
    "TECLADOS": teclados,
}

print('o print do pe do pedro é preto')

def escolher_produtos(saldo):
    carrinho = {}
    while True:
        print("Bem-vindo à loja PedralhaTEC, escolha entre as categorias disponíveis: HEADSETS - TECLADOS - MOUSES")
        escolha_categoria = input("Digite a categoria desejada ou 'Sair' para finalizar a compra: ").upper()
        

        if escolha_categoria == "SAIR":
            break

        if saldo >= 50:
            if escolha_categoria in categorias.keys():
                categoria = categorias[escolha_categoria]
                while True:
                    produtos = list(categoria.keys())
                    escolha_produto = input(f"Temos os seguintes {escolha_categoria.lower()} disponíveis: {produtos}, qual deseja comprar? ").title()

                    if escolha_produto in produtos:
                        while True:
                            try:
                                quantidade = int(input(f"Quantas unidades deseja comprar: "))
                                if quantidade <= 0:
                                    print("A quantidade deve ser maior que zero.")
                                else:
                                    break
                            except ValueError:
                                print("Insira somente números")

                        if escolha_produto in carrinho:
                            carrinho[escolha_produto]['quantidade'] += quantidade
                        else:
                            preco_produto = categoria[escolha_produto]
                            carrinho[escolha_produto] = {'quantidade': quantidade, 'preco_unitario': preco_produto}
                        
                        continuar = input("Deseja continuar comprando? (Sim/Não) ").title()
                        if continuar != "Sim":
                            break
                    else:
                        print("Insira um produto válido.")

        else:
            print("Seu saldo não é suficiente para comprar nenhum produto da loja")
            break


    print("Produtos no carrinho:")
    for produto, info_produto in carrinho.items():
        quantidade = info_produto['quantidade']
        preco_unitario = info_produto['preco_unitario']
        print(f"{quantidade} x {produto} (Preço unitário: {preco_unitario})")


    total = sum(info_produto['quantidade'] * info_produto['preco_unitario'] for info_produto in carrinho.values())


    print("Total da compra:", total)
    
    resp_parc = None
        
    if total > saldo:
        resp_parc = input("Seu saldo não é suficiente para comprar os produtos do carrinho, deseja parcelar? (S/N)").upper()

        while resp_parc not in ['S', 'N']:
            resp_parc = input("Insira somente S ou N!").upper()

        if resp_parc == 'S':
            while True:
                qtd_parcela_input = input("Temos opções de parcelamento de até 12x com juros de 1,7% ao mês, qual deseja escolher? ")
                try:
                    qtd_parcela = int(qtd_parcela_input)
                    if qtd_parcela < 1 or qtd_parcela > 12:
                        raise ValueError("A quantidade de parcelas deve estar entre 1 e 12.")
                    break
                except ValueError:
                    print("Por favor, insira um número inteiro válido para a quantidade de parcelas.")
                    continue

            taxa_juros = 1.7 / 100  
            valor_parcela_com_juros = total * ((1 + taxa_juros) ** qtd_parcela) / qtd_parcela
            total_com_juros = valor_parcela_com_juros * qtd_parcela

            print(f"Total da compra com juros: {total_com_juros:.2f}")
            print(f"Valor de cada parcela com juros: {valor_parcela_com_juros:.2f}")

            confirmacao = input("Deseja confirmar a compra? (S/N): ").upper()
            while confirmacao not in ['S', 'N']:
                confirmacao = input("Por favor, insira S para confirmar ou N para cancelar: ").upper()

            if confirmacao == 'N':
                resp_parc = 'S'
                
            elif confirmacao == 'S':
                print("Compra confirmada!")
        
        if resp_parc == 'N':
            print("Já que não deseja parcelar, sua compra será cancelada")

saldo = None

while True:
    try:
        numentrada = int(input("Insira um número "))
        saldo = numentrada
        break  
    except ValueError:
        print("Insira somente números!")
        
escolher_produtos(saldo)

