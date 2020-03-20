#!/usr/bin/python

import math
import os

os.system("clear")

'''
RUN-TIME COMPLEXITY: O(n)

Justification:
    Lines 43 - 46 are single operations 
        constituting  a RTC of  O(1)
    
    Line 49 - The loop itself has a RTC of O(n) 
        or O(n + m) where n and m represent two input sizes
        which can be reduced to O(n) as n+m constitute the 
        summation of both input sizes.
    Line 49 - The zip() function has a RTC of O(1)
            in Python 2 it would be O(n) --> (builds a new list)
            in Python 3 it would be O(n) --> (allocates an iterable 
                and assings a parameter array to an internal field)
            ref: https://stackoverflow.com/questions/36877715/what-is-the-time-complexity-of-zip-in-python
        both dict.items() in the loop have a RTC of O(1)
            in Python 2 it would be O(n) --> (builds a new list)
            in Python 3, it's O(1) -- (does not build a new list)
            ref: https://stackoverflow.com/questions/39219065/what-is-the-time-complexity-of-dict-keys-in-python
    Line 52 - append() has a RTC of O(1)
        ref: https://wiki.python.org/moin/TimeComplexity
    Line 59 - min() has an RTC of O(n)
        ref: https://wiki.python.org/moin/TimeComplexity

    Ignoring all O(1) RTC's, you are left with:
        O(n) for the loop, and O(n) for finding the min
        giving us O(n+n), or O(2n) which can be reduced 
        down to O(n)

'''


def recipe_batches(recipe, ingredients):
    # check for equal sets of ingredients
    if len(ingredients) != len(recipe):
        return 0

    ing_count = []

    # loop through both recipes and ingredients simultaneously
    for rec, ing in zip(recipe.items(), ingredients.items()):
        # append the number of quantities for each recipe ingredient
        # that can be made using the quantity of each ingredient available
        ing_count.append(ing[1] // rec[1])

    # return the smallest count in the ingredients count to represent
    # the minimum amount of servings for each recipe that can be made.
    # ...if it's any other number or the max, you run the risk of not
    # being able to make the number of servings without running out of
    # an ingredient with less serving quantities available
    return min(ing_count)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
