#   Create a list of integers. 
# Use a list comprehension to build a new list containing the squares of only the even numbers from the original list. Print both lists. 
# Save it as ex07b.py and let me know  
#   when you’re ready for review.        

nums=[12,445,33,4,23,3,343,34,34,3,333,44,3,333]
nums_sr=[n*n for n in nums if n % 2==0]
print(nums)
print(nums_sr)
