import timeit

text = 'what have the romans ever done for us'

def caps_comp():
    capitals = [char.upper() for char in text]
    return capitals

def caps_map():
    map_capitals = list(map(str.upper, text))
    return map_capitals

def words_comp():
    words = [word.upper() for word in text.split(' ')]
    return words

def words_map():
    map_words = list(map(str.upper, text.split(' ')))
    return map_words

if __name__ == '__main__':
    print('Caps_comp: {}'.format(timeit.timeit(caps_comp, number=10000)))
    print('Caps_map: {}'.format(timeit.timeit(caps_map, number=10000)))
    print('Words_comp: {}'.format(timeit.timeit(words_comp, number=10000)))
    print('Words_map: {}'.format(timeit.timeit(words_map, number=10000)))
