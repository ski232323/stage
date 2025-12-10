numbers = []

"""
def factorial():
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
"""

exp = 1


def factorial_recursive(n):
    if n == 0:
        return 1
    return factorial_recursive(n - 1) * n


for i in range (10):
    print(factorial_recursive(i))

"""fact(5):
    fact(4):
        fact(3):
            fact(2):
                fact(1):
                    fact(0):
                        1
                    1
                2
            6
        2
        
        """
