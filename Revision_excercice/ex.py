numbers = [1, 2, 3, 2, 4, 1, 5, 1]

def numbers_more(list):
    first = []
    second = []
    final = []
    for i in list:
        first.append(i)

    for j in list:
        second.append(j)

    for e in list:
        if i == j:
            final.append(i)
    print(final)



numbers_more(numbers)