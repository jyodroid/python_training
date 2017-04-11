import sys
import time
import psutil
import os
from ecdsa import SigningKey, NIST192p, NIST224p


def sign_192(text):
    signature_key = SigningKey.generate(curve=NIST192p)
    sign(text, signature_key)


def sign_224(text):
    signature_key = SigningKey.generate(curve=NIST224p)
    sign(text, signature_key)


def sign(text, signature_key):
    # for stats
    psutil.cpu_percent(interval=None)
    start_time = time.time()
    process = psutil.Process(os.getpid())
    a = process.memory_percent()

    # sign text
    signature = signature_key.sign(text)
    end_time = time.time()

    print ("signature: %s" % signature)
    print("--- time to sign %0.5f seconds---" % (end_time - start_time))
    # When interval is 0.0 or None compares system CPU times elapsed since last
    # call
    print("--- CPU Used %0.2f%%---" % psutil.cpu_percent(interval=None))
    print("--- Memory Used %0.6f%%---" % process.memory_percent())


# sig_file: toma un archivo con texto y firma digitalmente el texto
# @autor: John Jairo Tangarife Abril 6 del 2017
def main():
    if len(sys.argv) != 3:
        print 'usage: ./sign_file.py {--192 | --224} filename'
        sys.exit(1)

    filename = sys.argv[2]

    # r for read and U Will ignore DOS line ending versus Unix line ending
    my_file = open(filename, 'rU')

    # read file into one string
    text = my_file.read()

    my_file.close()

    option = sys.argv[1]
    if option == '--192':
        sign_192(text)
    elif option == '--224':
        sign_224(text)
    else:
        print 'unknown option: ' + option
        sys.exit(1)

if __name__ == '__main__':
    main()
