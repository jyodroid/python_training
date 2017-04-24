def happyNumber(n):

    # 1 <= n <= 2^31 - 1 == 2,147,483,647 Mersenne prime.
    # the maximum positive value for a 32-bit signed binary integer
    if n <= 0:
        return False

    for count in range (0, 6):
        # Split number
        suma = 0;
        while n > 0:
            # Add square number
            digit = (n % 10)
            suma += digit * 2
            n /= 10

        if suma == 1:
            return True

        n = suma
    return False

def main():
    print happyNumber(19)
    print happyNumber(1)
    print happyNumber(10)
    print happyNumber(9)
    print happyNumber(17)
    print happyNumber(1859631248)
    print happyNumber(1563712137)
    print happyNumber(8399)

if __name__ == '__main__':
    main()
