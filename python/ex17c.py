#  EX17C - MERGE WITH SUMMING (like warehouses)

#   You have two inventory dictionaries. Merge them - when the same key exists in both, ADD the counts together.

#   inventory_a = {"apple": 5, "banana": 3}
#   inventory_b = {"apple": 2, "orange": 4}

#   # TODO: Merge both, summing counts when same key exists
#   merged =

#   print(merged)

#   Expected output:
#   {'apple': 7, 'banana': 3, 'orange': 4}

#   CODE IT.

inventory_a = {"apple": 5, "banana": 3}
inventory_b = {"apple": 2, "orange": 4}
summed={}

for key,val in inventory_a.items():
    summed[key]=val

for key,val in inventory_b.items():
    summed[key]=summed.get(key,0)+val

print(summed)
