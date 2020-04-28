'''
	Find the maximum sum of the hourglass pattern in a 6x6 array.
'''
import numpy as np

def main(a):
    '''
        There are 16 hourglass patterns in a 6x6 array.
        Format of an hourglass pattern:
            a b c
              d
            e f g
        The goal is to find the maximum sum of an hourglass pattern.

        @param a - 6x6 integer array

        @return the maximum sum of hourglass patterns
    '''

    hourglass_max = float('-inf')
    sum_elements = 0
	
    for i in range(len(a) - 2):
        for j in range(len(a[i]) - 2):
            sum_elements = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] + a[i+2][j] + a[i+2][j+1] + a[i+2][j+2]
            if sum_elements > hourglass_max:
                hourglass_max = sum_elements

    print(hourglass_max)
    return hourglass_max

if __name__ == '__main__':
    a = np.array(
        [
            [1,1,1,0,0,0],
            [0,1,0,0,0,0],
            [1,1,1,0,0,0],
            [0,0,2,4,4,0],
            [0,0,0,2,0,0],
            [0,0,1,2,4,0]
        ])
    main(a)
