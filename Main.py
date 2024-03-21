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

def mostrar_categorias():
    print("Bem-vindo à loja PedralhaTEC, escolha entre as categorias disponíveis: HEADSETS - TECLADOS - MOUSES")

def selecionar_categoria():
    while True:
        escolha_categoria = input("Digite a categoria desejada ou 'Sair' para finalizar a compra: ").upper()
        if escolha_categoria == "SAIR":
            return None
        elif escolha_categoria in categorias.keys():
            return escolha_categoria
        else:
            print("Categoria inválida. Por favor, escolha uma categoria válida.")

def escolher_produto(categoria):
    categoria_dict = categorias[categoria]
    while True:
        produtos = list(categoria_dict.keys())
        escolha_produto = input(f"Temos os seguintes {categoria.lower()} disponíveis: {produtos}, qual deseja comprar? ").title()

        if escolha_produto in produtos:
            while True:
                try:
                    quantidade = int(input(f"Quantas unidades deseja comprar: "))
                    if quantidade <= 0:
                        print("A quantidade deve ser maior que zero.")
                    else:
                        return escolha_produto, quantidade
                except ValueError:
                    print("Insira somente números")

        else:
            print("Insira um produto válido.")

def calcular_total(carrinho):
    return sum(info_produto['quantidade'] * info_produto['preco_unitario'] for info_produto in carrinho.values())

def mostrar_carrinho(carrinho):
    print("Produtos no carrinho:")
    for produto, info_produto in carrinho.items():
        quantidade = info_produto['quantidade']
        preco_unitario = info_produto['preco_unitario']
        print(f"{quantidade} x {produto} (Preço unitário: {preco_unitario})")

def calcular_parcelas(total):
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

    return total_com_juros, valor_parcela_com_juros

def confirmar_compra(total_compra):
    confirmacao = input("Deseja confirmar a compra? (S/N): ").upper()
    while confirmacao not in ['S', 'N']:
        confirmacao = input("Por favor, insira S para confirmar ou N para cancelar: ").upper()

    if confirmacao == 'S':
        print("Compra confirmada!")
    else:
        print("Compra cancelada.")

def escolher_produtos(saldo):
    carrinho = {}

    mostrar_categorias()
    escolha_categoria = selecionar_categoria()

    if escolha_categoria is None:
        print("Compra cancelada.")
        return

    if saldo < 50:
        print("Seu saldo não é suficiente para comprar nenhum produto da loja.")
        return

    categoria = categorias[escolha_categoria]
    while True:
        escolha_produto, quantidade = escolher_produto(escolha_categoria)
        preco_produto = categoria[escolha_produto]

        if escolha_produto in carrinho:
            carrinho[escolha_produto]['quantidade'] += quantidade
        else:
            carrinho[escolha_produto] = {'quantidade': quantidade, 'preco_unitario': preco_produto}

        continuar = input("Deseja continuar comprando? (Sim/Não) ").title()
        if continuar != "Sim":
            break

    mostrar_carrinho(carrinho)

    total = calcular_total(carrinho)
    print("Total da compra:", total)

    if total > saldo:
        resp_parc = input("Seu saldo não é suficiente para comprar os produtos do carrinho, deseja parcelar? (S/N)").upper()

        while resp_parc not in ['S', 'N']:
            resp_parc = input("Insira somente S ou N!").upper()

        if resp_parc == 'S':
            total_com_juros, valor_parcela_com_juros = calcular_parcelas(total)
            print(f"Total da compra com juros: {total_com_juros:.2f}")
            print(f"Valor de cada parcela com juros: {valor_parcela_com_juros:.2f}")

            confirmar_compra(total_com_juros)
        else:
            print("Compra cancelada.")
    else:
        confirmar_compra(total)

saldo = None

while True:
    try:
        numentrada = int(input("Insira um número: "))
        saldo = numentrada
        break  
    except ValueError:
        print("Insira somente números!")

escolher_produtos(saldo)


