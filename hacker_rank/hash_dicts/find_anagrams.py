'''
    Given a string, find the number of substrings that are anagrams of each other
    Anagram = letters in one string can be rearranged to form another string.
'''

from collections import Counter

def main(s):
    '''
        @param s - lowercase string for which anagrams need to be found

        @return number of anagrams from substrings of s
    '''

    count = 0
    for i in range(len(s)):
    # Step 1: Traverse all possible substrings within a string
        a = []
        for j in range(len(s)-i):
            a.append(''.join(sorted(s[j:j+i+1])))


    # Step 2: Check in any 2 substrings of equal length are anagrams
        '''
            Counter extracts the elements into a dictionary
                b[key] = element
                b[val] = #occurences of that element
        '''
        b = Counter(a)

        '''
            sums #occurences through the keys (elements)
            "n choose 2" -> binomial distribution used: n(n-1)/2
        '''
        for j in b:
            count += ( b[j]*(b[j]-1) ) / 2

    print(int(count))
    return int(count)


if __name__ == '__main__':
    s = 'abad' # returns 2 (a,a), (ab,ba)
    main(s)
