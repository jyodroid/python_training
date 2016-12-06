import urllib


def read_text():

    # An instance of file
    quotes = open("./movie_quotes.txt")
    content_of_quotes = quotes.read()
    print(content_of_quotes)
    quotes.close()
    check_profanity(content_of_quotes)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" +
                                text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("profanity alert!!")
    elif "false" in output:
        print("This documet has no course words")
    else:
        print("Documet not readed properly")

read_text()
