def fizz_buzz(fizz_num, fizz_tag, buzz_num, buzz_tag):    
    for x in range(1,101):
        y = ''
        if x % fizz_num == 0:
            y += fizz_tag
        if x % buzz_num == 0:
            y += buzz_tag
        elif y == '':
            y = x
        print(f'Wow! The number {x} is actually {y}!')

def main():
    fizz_buzz(3, 'Fizz', 5, 'Buzz')

if __name__ == "__main__":
    main()