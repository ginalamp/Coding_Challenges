'''
    Given an array of integers, return the number of matching pairs.
    (Sock Merchant Problem)
'''
def main(a):
    '''
        @param a - an array of integers
        @return the number of matching pairs
    '''
    n = len(a)
    a = sorted(a)

    num_pairs = 0
    skipped = False
    for i in range(n - 1):
        if skipped:
            skipped = False
            continue
        if a[i] == a[i+1]:
            num += 1
            skipped = True
            continue

    return num

if __name__ == '__main__':
    a = [10,20,20,10,10,30,50,10,20]
    main(a)

