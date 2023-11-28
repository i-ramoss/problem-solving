qtd_pedidos = int(input())

while qtd_pedidos != 0:
    maximo_pizzas = int(input())

    solucao = [[0 for _ in range(maximo_pizzas + 1)] for _ in range(qtd_pedidos + 1)]

    tempo_dos_pedidos = []
    qtd_pizzas_pedido = []

    for _ in range(qtd_pedidos):
        tempo_do_pedido, qtd_pizza_pedido = input().split()

        tempo_dos_pedidos.append(int(tempo_do_pedido))
        qtd_pizzas_pedido.append(int(qtd_pizza_pedido))

    for i in range(1, qtd_pedidos + 1):
        for j in range(1, maximo_pizzas + 1):
            if qtd_pizzas_pedido[i - 1] > j:
                solucao[i][j] = solucao[i - 1][j]

            else:
                case1 = solucao[i - 1][j]
                case2 = (
                    tempo_dos_pedidos[i - 1]
                    + solucao[i - 1][j - qtd_pizzas_pedido[i - 1]]
                )

                if case1 >= case2:
                    solucao[i][j] = case1
                else:
                    solucao[i][j] = case2

    tempo_maximo = solucao[qtd_pedidos][maximo_pizzas]

    print(f"{tempo_maximo} min.")

    qtd_pedidos = int(input())
