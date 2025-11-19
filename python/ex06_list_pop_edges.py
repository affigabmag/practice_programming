#   Exercise 6 – Lists
#   Given a list of strings, remove the first and last items using pop, then print the remaining    
#   list and the two removed values.   

strs=[
    'gabi',
    'sammy',
    'david',
    'moshe',
    'tomer'
]

removed_strs=[strs.pop(0),strs.pop(-1)]
print(removed_strs)

print(strs)
