entry = input().split()
numbers = [int(numero) for numero in entry]


def reverseArray(a):
    initial = 0
    last = len(a) - 1

    for _ in range((len(a) // 2)):
        auxiliar = a[initial]
        a[initial] = a[last]
        a[last] = auxiliar

        initial += 1
        last -= 1

    return a


reverseArray(numbers)
print(numbers)
