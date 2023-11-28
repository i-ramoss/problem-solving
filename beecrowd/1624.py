qtd_produtos = int(input())

while qtd_produtos != 0:
    precos_produtos = []
    pesos_produtos = []

    for _ in range(qtd_produtos):
        preco, peso = input().split()

        precos_produtos.append(int(preco))
        pesos_produtos.append(int(peso))

    peso_maximo = int(input())

    solucao = [[0 for _ in range(peso_maximo + 1)] for _ in range(qtd_produtos + 1)]

    for i in range(1, qtd_produtos + 1):
        for j in range(1, peso_maximo + 1):
            if pesos_produtos[i - 1] > j:
                solucao[i][j] = solucao[i - 1][j]

            else:
                case1 = solucao[i - 1][j]
                case2 = (
                    precos_produtos[i - 1] + solucao[i - 1][j - pesos_produtos[i - 1]]
                )

                if case1 >= case2:
                    solucao[i][j] = case1
                else:
                    solucao[i][j] = case2

    tempo_maximo = solucao[qtd_produtos][peso_maximo]

    print(tempo_maximo)

    qtd_produtos = int(input())
