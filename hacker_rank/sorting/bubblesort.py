'''
    Implement bubblesort and print number of swaps needed, and
    first and last element in sorted array
'''

def main(a):
    '''
        @param a - array that needs to be sorted
    '''
    swaps = 0

    for i in range(len(a)):
        for j in range(len(a) - 1):
            # swap adjacent elements if they are in decreasing order
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                swaps += 1
    first = a[0]
    last = a[-1]
    print("Array is sorted in {} swaps.".format(swaps))
    print("First Element: {}".format(first))
    print("Last Element: {}".format(last))


if __name__ == '__main__':
    a = [6,4,1]
    a = [3,2,1]
    main(a)
