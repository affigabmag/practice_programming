#  Last drill for today (Exercise 10 style): 
# create a list of numbers (nums). 
# Make another list of the same length filled with zeros (zeros = [0] * len(nums)). 
# Replace each zero with the product of its index and the corresponding number from nums. 
# Do it with a loop or comprehension, 
# then print original and transformed lists. 
# Save as ex10b.py and let me know when it’s ready. After that we’ll have reinforced all ten.         


nums=[12,4545,45,445,65,6,6,556,5,5,65]
nums2=[]
for idx in nums:
    nums2.insert(idx,0)


print(nums)
print(nums2)