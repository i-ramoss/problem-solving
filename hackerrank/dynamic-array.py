local_queries = []

n, q = input().rstrip().split()
n = int(n)
q = int(q)

for _ in range(int(q)):
    line = input().rstrip().split()
    line_integers = [int(number) for number in line]
    local_queries.append(line_integers)


def dynamicArray(n, queries):
    array = []
    for _ in range(int(n)):
        array.append([])

    idx = None
    last_answer = 0
    answers = []

    for line in range(q):
        x = queries[line][1]
        y = queries[line][2]
        idx = (x ^ last_answer) % n

        if queries[line][0] == 1:
            array[idx].append(queries[line][2])

        elif queries[line][0] == 2:
            last_answer = array[idx][y % len(array[idx])]
            answers.append(last_answer)

    return answers
