def fizz_buzz(fizz_num, fizz_tag, buzz_num, buzz_tag, num_range): 
    """My fizzbuzz example with functions!

    Agrs:
        fizz_num: the fizz number
        fizz_tag: the fizz name for the number
        buzz_num: the buzz number
        buzz_tag: the buzz name for the number
        num_range: the range you want to count to

    Returns:
        print statement of fizz and buzz based on parameters
    """   
    for x in range(1,num_range + 1):
        y = ''
        if x % fizz_num == 0:
            y += fizz_tag
        if x % buzz_num == 0:
            y += buzz_tag
        elif y == '':
            y = x
        print(f'Wow! The number {x} is actually {y}!')

def main():
    fizz_buzz(3, 'Fizz', 5, 'Buzz', 100)

if __name__ == "__main__":
    main()