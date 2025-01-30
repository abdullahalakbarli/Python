from functools import reduce

fruits = {"Grape":(4, 6, 2), "Lemon":(7, 3, 1), "Orange":(5, 8, 1), "Apple":(2, 8, 10), "Watermelon":(0, 9, 6)}


# Code for Checkpoint 1 goes here.
total_fruits = reduce(lambda x, y: x + y, map(lambda q: fruits[q][0] + fruits[q][1] + fruits[q][2] , fruits))
print(total_fruits)
