#  EX17E - FIND COMMON KEYS

#   You have two dictionaries. Find which keys exist in BOTH.

#   dict_a = {"apple": 5, "banana": 3, "cherry": 2}
#   dict_b = {"apple": 2, "orange": 4, "cherry": 1}

#   # TODO: Find keys that exist in both dicts
#   common =

#   print(common)

#   Expected output:
#   ['apple', 'cherry']

#   Use set operation: set(dict_a) & set(dict_b)

dict_a = {"apple": 5, "banana": 3, "cherry": 2}
dict_b = {"apple": 2, "orange": 4, "cherry": 1}
common=set(dict_a) & set(dict_b)

print(common)