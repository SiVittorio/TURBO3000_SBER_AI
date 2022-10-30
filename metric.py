#pip install strsimpy
#pip install easyocr

from strsimpy.weighted_levenshtein import WeightedLevenshtein
import easyocr

reader = easyocr.Reader(['ru', 'en'])


#bounds = reader.readtext("./norm.jpg", paragraph=True) 
def insertion_cost(char):
    return 1.0


def deletion_cost(char):
    return 1.0


def substitution_cost(char_a, char_b):
    if char_a == 't' and char_b == 'r':
        return 0.5
    return 1.0

weighted_levenshtein = WeightedLevenshtein(
    substitution_cost_fn=substitution_cost,
    insertion_cost_fn=insertion_cost,
    deletion_cost_fn=deletion_cost)

bounds = reader.readtext("<ПУТЬ К ФАЙЛУ>", paragraph=True)

for i in range(len(bounds)):
    print(1 - (weighted_levenshtein.distance(bounds[i][1], '<ИСТИННАЯ СТРОКА>')) /
               max(len(bounds[i][1]), len('<ИСТИННАЯ СТРОКА>')))
