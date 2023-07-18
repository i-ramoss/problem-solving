def introTutorial(key, array):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if key == array[mid]:
            return mid
        elif key < array[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


example = [1, 4, 5, 7, 9, 12]
key = 7

print("Index:", introTutorial(key, example))
