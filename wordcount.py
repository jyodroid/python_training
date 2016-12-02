from operator import itemgetter


def count_words(words, top):
    words_count = {}
    for word in words.split():
        if word in words_count:
            words_count[word] = words_count[word] + 1
        else:
            words_count[word] = 1

    sorted_words_count = sorted(words_count.items(), key=itemgetter(0))

    sorted_words_count = sorted(
        sorted_words_count, key=itemgetter(1), reverse=True)

    top_n = sorted_words_count[:top]
    return top_n

def test_run():
    print count_words("cat bat mat cat bat cat", 3)
    print count_words(
        "betty bougth a bit of butter but the butter was bitter", 3)
    print count_words("the nigth is dak and full of terrors", 8)

if __name__ == '__main__':
    test_run()
