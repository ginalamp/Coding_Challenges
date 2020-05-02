'''
    Given an unsorted array with consecutive integers, this program
    sorts the array and prints the minimum amount of swaps needed
    to sort the array
'''

def main(arr):
    '''
        @param arr - an array of consecutive integers (unsorted)

        @return the minimum amount of swaps needed to sort the given array
    '''

    # temp is  an array where the values are the indexes
    # If one accesses temp[val], one would get the index (i) as output
    # The index in this case would be the expected value - 1
    temp = {val: i for i, val in enumerate(arr)}

    min_swaps = 0

    for i in range(len(arr)):
        value = arr[i]

        # array contains consecutive integers starting from 1
        expected_value = i + 1

        # get the index of the value wanted
        expected_i = temp[expected_value]

        # swap values if not in the correct order
        if value != expected_value:
            # in the main array: swap current with the value wanted at the current index
            arr[i] = expected_value
            arr[expected_i] = value
            # in the enum array: swap current with the value wanted at the current index
            temp[value] = expected_i
            temp[expected_value] = i

            min_swaps += 1

    print(min_swaps)
    return min_swaps




if __name__ == '__main__':
    arr = [1,3,5,2,4,6,7]
    main(arr)
