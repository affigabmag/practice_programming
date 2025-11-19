#  Create a list of six strings. 
# Use pop(0) and pop(-1) to remove the first and last items, 
# store them in a tuple or list, 
# and print the removed pair plus the remaining list. 
# Repeat that process once more (so you remove two pairs total), 
# printing each step. 
# Save as ex06b.py and ping me when ready. 

strs =[
    "str1",
    "gabiddddd",
    "haimddd dddd",
    "sisisis  ssilsbi",
    "ron  fffffffff",
    "asasas ofir"
]

strs_removed=[strs.pop(0),strs.pop(-1)]
print(strs)
print(strs_removed, len(strs_removed))

strs_removed=[strs.pop(0),strs.pop(-1)]
print(strs)
print(strs_removed, len(strs_removed))

