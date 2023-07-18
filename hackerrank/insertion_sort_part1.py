def insertionSort1(n, arr):
    j = n - 1
    key = arr[j]

    while j > 0 and key < arr[j - 1]:
        arr[j] = arr[j - 1]

        for k in arr:
            print(k, end=" ")
        print()

        j -= 1

    arr[j] = key

    for k in arr:
        print(k, end=" ")
    print()


example1 = [2, 4, 6, 8, 3]
n1 = 5
example2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
n2 = 10

insertionSort1(n2, example2)
