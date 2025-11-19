#   Next drill (Exercise 9 style): 
# have a list of strings, 
# loop with enumerate, 
# but start counting at 1 (use enumerate(strings, start=1)). 
# Print each item as 01: value, 02: value, etc. 
# Use str(idx).zfill(2) for the padded numbers. Save as ex09b.py and let me know when you want it reviewed. 

strs=[
    'gabi',
    'favid',
    'moshe',
    'reoven',
    'liran',
    'sami',
    'esti'
]

for idx,sstr in enumerate(strs,1):
    print(f'{str(idx).zfill(2)}: {sstr}')