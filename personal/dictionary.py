import sys


def loopDictionary(dictionary):
    print "Just the keys"
    print dictionary.keys()
    print "Just the values"
    print dictionary.values()

    # iterate
    for key in dictionary.keys():
        print '%s -> %s' % (key, dictionary.get(key))

    # print in tuples
    print sortedictionary.items()


def Cat(filename):

    # r for read and U Will ignore DOS line ending versus Unix line ending
    my_file = open(filename, 'rU')
    # read file as a python list of lines
    # lines = my_file.readlines()
    # print lines

    # for line in file:
    # the coma will hide the line ending
    # print line,

    # read file into one string
    text = my_file.read()
    print text,

    my_file.close()


def test_run():
    # definition
    d = {}
    d['a'] = "alpha"
    d['o'] = "omega"
    d['g'] = "gama"

    print d['a']
    print d.get('a')
    print d.get('z')
    print d.get('z') is None
    print 'z' in d
    print 'a' in d

    loopDictionary(d)

    Cat("small.txt")

if __name__ == '__main__':
    test_run()
