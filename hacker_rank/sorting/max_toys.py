'''
    Given a list of toy prices and a budget, this program maximises the amount of
    toys that can be bought with the budget.
'''

def main(toy_prices, budget):
    '''
        @param toy_prices - an int array with toy prices
        @param budget - the maximum amount that the buyer can spend

        @return the maximum amount of toys that can be bought given the budget
    '''

    toy_prices = sorted(toy_prices)
    num_toys = 0

    for i in range(len(toy_prices)):
        valid_purchase = budget - toy_prices[i]
        if valid_purchase >= 0:
            budget -= toy_prices[i]
            num_toys += 1

    print(num_toys)
    return num_toys

if __name__ == '__main__':
    toy_prices = [1,12,5,111,200,1000,10]
    budget = 50

    main(toy_prices, budget)
