import math
import random


def prime_number(number):
    for var in range(2, int(math.sqrt(number))+1):
        if number % var == 0:
            return False
    return True


def prime_number_print(number):
    for var in range(2, int(math.sqrt(number))+1):
        if number % var == 0:
            return "%d not prime because can be divide by %d" % (number, var)
    return "%d is prime" % (number)


def test_run():

    random_num = random.randint(0, 100)
    print prime_number_print(random_num)

if __name__ == '__main__':
    test_run()
