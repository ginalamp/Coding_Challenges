'''
   Need to deduce whether a ransom can be created from whole words available in a magazine
'''
def main(magazine, ransom):
    '''
        @param magazine - an array of Strings (words available)
        @param ransom - an array of Strings (message wish to form)

        @output print "Yes" or "No" (depending on whether the ransom could be formed from the words in the magazine)
    '''

    temp = []
    for word in ransom:
        if word in magazine:
            magazine.remove(word)
            temp.append(word)
        else:
            print("No")
            break

    if len(ransom) == len(temp):
        print("Yes")

    # NOTE: issubset does not cater for duplicates (e.g. ransom = ["a", "a", "b"] and magazine = ["a", "b"] will return True
    # if set(ransom).issubset(magazine):
    #    print("Yes")


if __name__ == '__main__':
    magazine = ["word2", "word1"]
    ransom = ["word1", "word2", "word1"]
    main(magazine, ransom)
