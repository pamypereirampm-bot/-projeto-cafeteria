produtos = {}
clientes = {}
pedidos = []

while True:
    operacao = input("1=produto 2=cliente 3=pedido 4=listar 0=sair: ")
    if operacao=='1': produtos[input("nome: ")] = float(input("preço: "))
    elif operacao=='2': clientes[input("nome: ")] = input("contato: ")
    elif operacao == '3':
        c = input("cliente: ")
        p = input("produto: ")
        if c in clientes and p in produtos:
            pedidos.append((c, p))
            print("ok")
        else:
            print("cadastre cliente/produto")
    elif operacao=='4': print("produtos:",produtos,"clientes:",clientes,"pedidos:",pedidos)
    elif operacao=='0': break
