# This is a script to find the fibonacci sequence
def fibonacci(n):
    if n ==0 or n==1 :
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


for i in range(50):
    print(i,fibonacci(i))

