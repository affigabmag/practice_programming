#   Next up (Exercise 8 style): 
# create a list of five floats (hardcode or prompt). 
# Compute the average with sum(list) / len(list) 
# and print a formatted string like Average: 12.34 using either f-strings  
#   or format. Also print the minimum and maximum with one decimal place. Save in ex08b.py and I’ll check it when ready.                  

numf=[
    12.12,
    45.454,
    443.676,
    65.56,
    333.45
    ]

print(f'avg is: {sum(numf)/len(numf):.2f}')
print(f'res     {min(numf):.1f}')
print(max(numf))
print(len(numf))