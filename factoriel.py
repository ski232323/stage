numbers = []


def factorial():
    global exp
    for n in range(10):
        numbers.append(n)
        location = numbers.index(n)
        numbers_before_n = numbers[:location]
        exp = 0
        for i in numbers_before_n:
            if i == 0:
                exp = 1
            else:
                exp = i * exp
        print(exp)


factorial()
