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
    for x in range(1, num_range + 1):
        y = ''
        if x % fizz_num == 0:
            y += fizz_tag
        if x % buzz_num == 0:
            y += buzz_tag
        elif y == '':
            y = x
        return f'Wow! The number {x} is actually {y}!'


def main():
    fb_ results = fizz_buzz(3, 'Fizz', 5, 'Buzz', 100)
    print(fb_results)
    

if __name__ == "__main__":
    main()
