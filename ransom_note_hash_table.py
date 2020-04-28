'''
   Need to deduce whether a ransom can be created from whole words available in a magazine
'''
def main(magazine, ransom):
    '''
        @param magazine - an array of Strings (words available)
        @param ransom - an array of Strings (message wish to form)

        @return "Yes" or "No" (depending on whether the ransom could be formed from the words in the magazine)
    '''

    if set(ransom).issubset(magazine):
        print("Yes")
        return "Yes"

    print("No")
    return "No"



if __name__ == '__main__':
    magazine = ["word2", "word3"]
    ransom = ["word1", "word2"]
    main(magazine, ransom)
