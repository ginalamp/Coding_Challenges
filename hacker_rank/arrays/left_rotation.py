'''
    Shift each element in an array to the left with a specified number of spaces.
'''

def main(a, shift):
    '''
        @param a - an array
        @param shift - number of spaces a needs to shift left by

        @return the shifted array
    '''
    shifted = a[shift:] + a[:shift]

    for i in shifted:
        print(i, end = " ")

    return shifted


if __name__ == '__main__':
    a = [1,2,3,4,5,6,7]
    shift = 4
    main(a, shift)
