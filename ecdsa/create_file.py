
import sys


def create_file(size, name):
    f = open(name, "wb")
    f.seek(int(size)-7)
    f.write("mensaje")
    f.close()


def main():
    if len(sys.argv) != 3:
        print 'usage: ./create_file.py filename size'
        sys.exit(1)
    size = sys.argv[2]
    filename = sys.argv[1]
    create_file(size, filename)

if __name__ == '__main__':
    main()
