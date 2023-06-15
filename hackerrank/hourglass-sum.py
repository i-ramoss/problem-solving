matriz = []

for _ in range(6):
    linha = input().split()
    linha_inteiros = [int(elemento) for elemento in linha]
    matriz.append(linha_inteiros)


def hourglassSum(arr):
    highest_sum = None

    for line in range(4):
        for column in range(4):
            # top
            current_sum = arr[line][column]
            current_sum += arr[line][column + 1]
            current_sum += arr[line][column + 2]

            # middle
            current_sum += arr[line + 1][column + 1]

            # bottom
            current_sum += arr[line + 2][column]
            current_sum += arr[line + 2][column + 1]
            current_sum += arr[line + 2][column + 2]

            if column == 0 and line == 0:
                highest_sum = current_sum
            elif current_sum > highest_sum:
                highest_sum = current_sum

    return highest_sum


print(hourglassSum(matriz))
