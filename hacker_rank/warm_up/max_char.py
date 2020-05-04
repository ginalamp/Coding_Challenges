'''
    Given a string, return the char that appears the max number of times in the string
    Ties settled by returning char that appeared first in string.
'''

from collections import Counter
import operator
def main(text):
    '''
        @param text String
        @return character that appears the most in text
    '''

    counter = Counter(list(text))
    counter = max(counter.items(), key=operator.itemgetter(1))[0]
    
    print(counter)
    return counter[0]


if __name__ == '__main__':
    text = 'helloworld'
    main(text)
