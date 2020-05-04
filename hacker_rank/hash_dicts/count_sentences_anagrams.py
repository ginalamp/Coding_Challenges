'''
   Find the number of combinations of words (and anagrams of those words)
   that can form a given sentence
'''
from collections import Counter
DEBUG = False


def countSentences(w, s):
    '''
        @param w - list of strings (single words)
        @param s - list of strings (sentences)

        @return the number of combinations of words (including anagrams
        that are in the list of words) that can form the given sentences

        Example input:
            w = ["the", "bats", "tabs", "in", "cat", "act"]
            s = ["cat the bats", "in the act", "act tabs in"]

            output: [4,2,4]
    '''

    count = []
    for x in range(len(s)):
        result = sentence_counter(s[x], w)
        count.append(result)

    for i in count:
        print(i)

    return count


def sentence_counter(s, w):
    '''
        @param w - list of strings (single words)
        @param s - a single string

        @return the number of combinations of words (including anagrams
        that are in the list of words) that can form the given sentence
    '''

    # sorted sentence
    sorted_sentence = sorted(s.split(" "))
    for i in range(len(sorted_sentence)):
        sorted_sentence[i] = ''.join(sorted(sorted_sentence[i]))

    # sorted words
    words = w
    for i in range(len(w)):
        words[i] = ''.join(sorted(words[i]))

    # no posible combinations
    if len(sorted_sentence) > len(words):
        if DEBUG:
            print("Length of string longer than length of word combinations")
        return 0

    # dictionary with number of occurences as values
    dict_words = Counter(words)
    dict_sentence = Counter(sorted_sentence)

    # sentence only contains unique words (set)
    set_s = list(set(sorted_sentence))

    '''
        Go through all unique words in the sentence and check whethe dict_words[] 
        contains that word. If dict_words[] contains the given word, the count
        is incremented according to the number of anagrams of that word  in words[]
        as well as the number of occurences of that word in the sentence.
    '''
    count = 0
    for i in range(len(set_s)):
        if set_s[i] in dict_words:
            if dict_words[set_s[i]] > 1:
                count += dict_words[set_s[i]]**dict_sentence[set_s[i]]
        else:
            if DEBUG:
                print("words[] does not contain all the words in the given sentence")
            return 0

    # if there are no anagrams in words[]
    if count == 0:
        count = 1

    return count


if __name__ == '__main__':

    # output = [4,2,4]
    words = ["the", "bats", "tabs", "in", "cat", "act"]
    sentences = ["cat the bats", "in the act", "act tabs in"]
    countSentences(words, sentences)

    # output = [1,9,3,12,6]
    words = ['star', 'tars', 'stay', 'tay', 'seed',
             'dees', 'eesd', 'rast', 'date', 'ate']
    sentences = ['ate date stay', 'rast tay star',
                 'tay stay tars', 'seed dees star', 'ate seed rast']
    countSentences(words, sentences)

    # output = [4,6]
    words = ["a", "a", "ba", "ab", "asd", "dsa", "sda", "das"]
    sentences = ["a ba", "ads a"]
    countSentences(words, sentences)
