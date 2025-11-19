#   Exercise 10 – Lists                                                                             
#   Create a list of numbers and another list of the same length filled with zeros. Replace each    
#   zero with the product of its index and the corresponding number from the first list. Example    
#   result format: if numbers is [5, 10, 15], transformed list becomes [0*5, 1*10, 2*15] ⇒ [0, 10,  
#   30]. Print both lists. Use a loop or comprehension—your choice. Save as ex10.py.     

nums=[2,4,4,8,7,45,34,445]
zeros=[0,0,0,0,0,0,0,0]

for idx,val in enumerate(nums):
    zeros[idx]= idx*val

print (nums)

print (zeros)