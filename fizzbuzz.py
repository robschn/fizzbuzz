for x in range(1,101):
    if x % 15 == 0:
        y = 'FizzBuzz'
    elif x % 3 == 0:
        y = 'Fizz'
    elif x % 5 == 0:
        y = 'Buzz'
    else:
        y = x
    print(f'I cannot believe {x} is actually {y}!')
