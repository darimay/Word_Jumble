from collections import defaultdict


def word_jumble(string, word_list):
    isalpha = str.isalpha
    letters_dict = defaultdict(int)
    string = filter(isalpha, string).lower()
    for letter in string:
        letters_dict[letter] += 1
    num_letters = len(string)
    jumble_words = []
    for word in word_list:
        word = filter(isalpha, word).lower()
        if word != string and len(word) <= num_letters:
            letters_dict_cp = dict(letters_dict)
            for letter in word:
                if letter in letters_dict_cp and \
                   letters_dict_cp[letter] > 0:
                    letters_dict_cp[letter] -= 1
                else:
                    break
            else:
                jumble_words.append(word)
    return jumble_words


# Test cases for word_jumle
def test(words_file='word_list.txt'):
    with open(words_file) as f:
        words = f.readlines()
        _word_jumble = lambda s: word_jumble(s, words)
        assert(_word_jumble('') == [])
        assert(_word_jumble('123') == [])
        assert(sorted(_word_jumble('dog')) == sorted(['god', 'do', 'go']))
        assert(sorted(_word_jumble('doG')) == sorted(['god', 'do', 'go']))
        assert(sorted(_word_jumble('Do3g')) == sorted(['god', 'do', 'go']))
        assert('hello' in _word_jumble('holLe'))
        assert('hello' not in _word_jumble('hole'))

        # Build a string input big enough so that
        # word_jumble returns the whole word list
        string = filter(str.isalpha, ''.join(words))
        from time import time
        t = time()
        jumbles = _word_jumble(string)
        print "Time it took to generate the full list: %.3f secs" % (time()-t)
        assert(len(jumbles) == len(words))
