#   Exercise 9 – Lists                                                                              
#   Create a list of strings. Use enumerate to print each item with its index in the format 0:      
#   value. No manual counters. Save as ex09.py.    

strs=[
    'gabi',
    'moshe',
    'reoven',
    'david',
    'silvi'
]

for idx,val in enumerate(strs):
    print(f"{idx}: {val}")