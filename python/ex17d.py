#  EX17D - FIND UNIQUE KEYS

#   You have two dictionaries. Find which keys exist only in the first one and which exist only in the second one.

#   dict_a = {"apple": 5, "banana": 3, "cherry": 2}
#   dict_b = {"apple": 2, "orange": 4, "grape": 1}

#   # TODO: Find keys only in dict_a
#   only_in_a =

#   # TODO: Find keys only in dict_b
#   only_in_b =

#   print(only_in_a)
#   print(only_in_b)

#   Expected output:
#   ['banana', 'cherry']
#   ['grape', 'orange']

#   Use set operations: set(dict_a) - set(dict_b)

#   CODE IT.

dict_a = {"apple": 5, "banana": 3, "cherry": 2}
dict_b = {"apple": 2, "orange": 4, "grape": 1}

# keys=[]
# c=0

# for key,val in dict_a.items():
#     keys.insert(c,key)

# for key,val in dict_b.items():
#     if key in keys:
#         keys.remove(key)
#     else:
#         keys.append(key)

# print(keys)

# for key1,val1 in dict_a.items():
#     for key2,val2 in dict_b.items():
#         if key2==key1:
#             dict_a[key1]="to remove"
#             dict_b[key2]="to remove"

# dict_a = {k: v for k, v in dict_a.items() if v != "to remove"}
# dict_b = {k: v for k, v in dict_b.items() if v != "to remove"}

# # d = {k: v for k, v in d.items() if v != 2}

# print(dict_a,dict_b)

only_in_a = sorted(set(dict_a) - set(dict_b))
only_in_b = sorted(set(dict_b) - set(dict_a))

print(only_in_a)
print(only_in_b)