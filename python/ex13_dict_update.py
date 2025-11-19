#   1. Starts with a dictionary named inventory mapping item names to counts (e.g., "apples": 5, "bananas": 2, "oranges": 0).                                                                              
#   2. Increase the value for at least one existing item (e.g., restock apples by +3).                                                                                                                     
#   3. Add a brand-new item with its count.                                                                                                                                                                
#   4. Remove one item using pop and print its removed value.                                                                                                                                              
#   5. Print the final dictionary to show all changes.   

inventory={
    "apples":5,
    "bananaes":2,
    "oranges":0,
    "melon":6,
    "pineapples":9
}

inventory["apples"]+=3

print(inventory)

inventory["watermelons"]=77
print(inventory)

removed=inventory.pop("oranges")

print(removed)
print(inventory)