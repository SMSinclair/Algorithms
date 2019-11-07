#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    max_batches = []
    for req in recipe.keys():
        if req not in ingredients.keys():
            return 0
        max_batches.append(ingredients[req]//recipe[req])
    return min(max_batches)



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))