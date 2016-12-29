def test_run():
    a = [(2, 'b'), (1, 'a'), (3, 'd')]
    print sorted(a)

    # Paralelo assigment
    (x, y) = (7, 9)
    print "x = " + str(x)
    print "y = " + str(y)

if __name__ == '__main__':
    test_run()
