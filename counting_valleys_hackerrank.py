'''
    Given the number of Up and Down steps taken by a hiker, this program returns the number of valleys walked through when the hiker starts at sea level.

    Starting and ending at sea level
        Mountain: up from sea level
        Valley: down from sea level
'''

def main(steps):
    '''
       @param array of steps taken (D = down; U = up)

       @return an integer denoting the number of valleys traversed

        Example input: [DDUUUUDD]
            1 valley (until level -2)
            1 mountain (until level 2)
            Back to sea level (level 0)
        Output: 1 valley
    '''

    n = len(steps)

    # start at sea level
    level = 0

    num_valleys = 0
    for step in steps:
        if step == 'D':
            if level == 0:
                num_valleys += 1
            level -= 1
        else:
            level += 1

    return num_valleys

if __name__ == '__main__':
    steps = ['DDUUUUDD']
    main(steps)
