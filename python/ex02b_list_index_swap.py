#   Create a list of six integers. 
#   Print the last element two ways: nums[len(nums) - 1] and nums[-1]. 
#   Then swap the last two values using indexing (no helper functions). 
#   Save it as ex02b.py and let me   

nums=[1,44,6,5,44,5]
last_num_a=nums[len(nums)-1]
last_num_b=nums[-1]

temp=nums[-1]
nums[-1]=nums[-2]
nums[-2]=temp

print(f"the numns are: \r\n 1st:{last_num_a}\r\n 2nd:{last_num_b}")
print(nums)
