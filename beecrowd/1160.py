numero_de_casos = int(input())


def calcular_tempo_em_anos(pop_a: int, pop_b: int, cresc_a: float, cresc_b: float):
    numero_de_anos = 0

    while pop_a <= pop_b:
        pop_a += int(pop_a * (cresc_a / 100))
        pop_b += int(pop_b * (cresc_b / 100))

        numero_de_anos += 1

        if numero_de_anos > 100:
            break

    if numero_de_anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{numero_de_anos} anos.")


for i in range(numero_de_casos):
    populacao_a, populacao_b, crescimento_a, crescimento_b = input().split()

    populacao_a = int(populacao_a)
    populacao_b = int(populacao_b)
    crescimento_a = float(crescimento_a)
    crescimento_b = float(crescimento_b)

    calcular_tempo_em_anos(populacao_a, populacao_b, crescimento_a, crescimento_b)
