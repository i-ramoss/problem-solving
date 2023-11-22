tamanho_lista = int(input())
valores = list(map(int, input().split()))

for index, valor in enumerate(valores):
    if index == 0:
        menor_valor = valor
        posicao = index

    if valor < menor_valor:
        menor_valor = valor
        posicao = index

print(f"Menor valor: {menor_valor}")
print(f"Posicao: {posicao}")
