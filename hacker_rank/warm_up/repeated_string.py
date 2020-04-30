'''
    Given a string, a letter and an integer n, find and print the number that the given letter occurs
    in the first n letters of the infinite string.

    The infinite string is defined as the given string that repeats an infinite amount of times.
    e.g. 'aba' would become 'abaabaabaabaabaabaaba...' an "infinite amount of times.
    If one needed to find the number of a's in the first n=10 indices, the result would be 7.

'''

def main(s, letter, n):
    '''
        @param s - a String
        @param letter - character that should be counted
        @param n - an integer indicating how many letters to search for in the "infinite String"

        @return the number of times the specified letter repeats within the first n letters of repeated s
    '''

    # multiply s until you get to the point where adding another instance of s would be greater than n
    result = s.count(letter) * (n // len(s))

    # count the number of the specified letter between n and the point whetre you stopped multiplying ^^
    remainder = s[ :(n % len(s)) ]

    result += remainder.count(letter)

    print(result)
    return result

if __name__ == '__main__':
    s = 'kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm'
    letter = 'a'
    n = 736778906400
    main(s, letter, n)
