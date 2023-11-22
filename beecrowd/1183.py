operacao = input()
matriz = []

for i in range(12):
    linha = []

    for j in range(12):
        linha.append(float(input()))

    matriz.append(linha)

soma = 0
qtd_elementos = 0

for i in range(12):
    for j in range(i + 1, 12):
        soma += matriz[i][j]
        qtd_elementos += 1

if operacao == "S":
    print(round(soma, 1))
elif operacao == "M":
    print(round(soma / qtd_elementos, 1))
