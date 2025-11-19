# EX17B - MERGE TWO DICTIONARIES

#   You have two dictionaries. Combine them into one new dictionary called merged.

#   dict1 = {"a": 1, "b": 2}
#   dict2 = {"c": 3, "d": 4}

#   # TODO: Merge dict1 and dict2 into merged
#   merged =

#   print(merged)

#   Expected output:
#   {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#   CODE IT.

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged={}

for key,value in dict1.items():
    print(key,value)
    merged[key]=value

for key,value in dict2.items():
    print(key,value)
    merged[key]=value
    
print(merged)


