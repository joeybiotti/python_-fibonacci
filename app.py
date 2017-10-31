def get_fib():
    count = int(input('How many fibonacci numbers do you want?'))
    i = 1
    if num == 0:
        fibonacci = []
    elif num == 1:
        fibonacci = [1]
    elif num == 2:
        fibonacci = [1, 1]
    elif num  > 2:
        fibonacci= [1, 1]
        while i < (count - 1):
            fibonacci.append(fibonacci[1] + fibonacci[i-1])
            i += 1
