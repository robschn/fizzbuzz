for x in range(1,101):
    y = ''
    if x % 3 == 0:
        y += 'Fizz'
    if x % 5 == 0:
        y += 'Buzz'
    if y == '':
        y = x
    print(f'Wow! The number {x} is actually {y}!')
