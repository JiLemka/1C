fib_1 = 0
fib_2 = 1
counter_end = int(input())

while counter_end > 0:
    print(f"{fib_1} ", end="\n")
    fib_1, fib_2 = fib_2, fib_1 + fib_2
    counter_end -= 1
