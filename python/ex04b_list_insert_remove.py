#   1. Start with any five integers in nums.                                                                                                                                                               
#   2. Replace the element at index 2 with a new value.                                                                                                                                                    
#   3. Insert another number at index 2 (so it becomes the new third element).                                                                                                                             
#   4. Remove the value that used to be third (you can store it before step 2 or just remove by value).                                                                                                    
#   5. Print after each step so you can see the list evolve.    

nums=[23,34,2222,343,44]
print(nums)

original_third = nums[2]
nums.append(original_third)  # keep original third value in the list for later removal

nums[2]=12
print(nums)

nums.insert(2,1231) 
print(nums)

nums.remove(original_third)
print(nums)
