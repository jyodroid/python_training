import prime


def add_lists(a, b):
    print a + b


def iterate_list(array):
    for element in array:
        print element


def reference(a):
    # list doesn't a copy, they references other lists
    c = a
    print "a:"
    print a
    print "c:"
    print c
    a[2] = 3
    print "a changed and c: "
    print c


def copy_lists(a):
    # you have to tell list to do a copy
    c = a[:]
    print "a:"
    print a
    print "c:"
    print c
    a[2] = 3
    print "a changed and c: "
    print c


def check(value, array):
    print value in array


def append_to_list(value, array):
    array.append(value)  # returns None (nothing)
    print array


def remove_to_list(index, array):
    print str(array.pop(index)) + ' removed'
    print array


def remove_to_list_2(index, array):
    print str(array[index]) + ' is about to be removed'
    del array[index]
    print array


def sort_list(array):
    print sorted(array)


def sort_list_reverse(array):
    print sorted(array, reverse=True)


def custom_sorted(array):
    # key requires a function of one argument
    print sorted(sorted(array), key=prime.prime_number)


def test_run():
    # lists can have mixed elements
    a = [2, 1, 'abc']
    print a
    print 'index of 1 = %d' % (a.index(1))
    print len(a)
    print "list without last element"
    print a[:-1]

    # lists can add other lists
    print "add ['d', 'e'] to a"
    add_lists(a, ['d', 'e'])
    print 'reference a'
    reference(a)
    print 'copy a'
    a = [2, 1, 'abc']
    copy_lists(a)
    print 'a iterated'
    iterate_list(a)
    print 'check if 2 is in a'
    check(2, a)
    print 'append 4 to a'
    append_to_list(4, a)
    print 'remove 4 to a'
    remove_to_list(-1, a)
    print 'remove 3 to a'
    remove_to_list_2(-1, a)

    # sorting
    b = [15, 4, 8, 23, 9, 12, 17, 13]
    print 'b:'
    print b

    print 'sorted b:'
    sort_list(b)

    print 'reverse sorted b:'
    sort_list_reverse(b)

    print 'custom sorted (last prime numbers) b:'
    custom_sorted(b)

    c = ['S', 't', 'r', 'i', 'n', 'g', 'B', 'u', 'i', 'l', 'd', 'e', 'r']
    print 'c:'
    print c
    print 'c as string:'
    print ''.join(c)
    print 'c as string with token & = d:'
    d = '&'.join(c)
    print d
    print 'd split by token &:'
    print d.split('&')

    # delete a
    del a

if __name__ == '__main__':
    test_run()
