#   Create ex14_dict_iteration.py with these steps:
                                                                                                                                                                                                         
#   1. Define a dictionary scores mapping student names to integer scores (at least four entries).                                                                                                         
#   2. Use a for loop to print each student and their score, e.g., Alice: 88.                                                                                                                              
#   3. Calculate the average score and print it formatted to two decimal places.                                                                                                                           
#   4. Also find and print the student with the highest score (you can track it during the loop or use max(scores, key=scores.get)).     

scores={
    'gabi':98,
    'ron':100,
    'david':87,
    'haim':66,
    'moshe':56
}

summ=0
maxx=0

for key in scores:
    value=scores[key]
    summ+=value
    if value>maxx:
        maxx=value
    
avgg=summ/len(scores)

print(f"{avgg:.2f}")
print(scores)
print("max val: ",maxx)
