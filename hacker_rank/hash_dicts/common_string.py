'''
    Given two strings, determine if they share a common substring.
    min(len(substring)) == 1
'''

def main(s1, s2):
    '''
        @param s1, s2 - the two strings to analyse
        @return YES/NO indicating whether the strings share a common substring
    '''

    # iterate through the shorter string
    if (len(s1) > len(s2)):
        temp = s1
        s1 = s2
        s2 = temp

    for i in s1:
        if i in s2:
            print("YES")
            return "YES"

    print("NO")
    return "NO"


if __name__ == '__main__':
    s1 = 'a'
    s2 = 'ab'
    main(s1, s2)
