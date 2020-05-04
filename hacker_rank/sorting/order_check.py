'''
    Given a list of integers, determine amount of elements not 
    in the correct order (the list should be in assending order)
'''
def main(height):
    '''
        @param list of integers
        @return number of elements out of order
    '''

    count = 0
    sorted_height = sorted(height)

    for i in range(len(height)):
        if height[i] != sorted_height[i]:
            count += 1

    print(count)
    return(count)


if __name__ == '__main__':
    height = [1,1,3,3,4,1] #should return 3
    main()
