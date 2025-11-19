#  Create ex_mix01.py and implement the following steps in order, printing after each so you can see the progression:
                                                                                                                                                                                                         
#   1. Start with a list of eight integers (any values). Print it.                                                                                                                                         
#   2. Use enumerate(..., start=1) to print each item as 01: value, etc.                                                                                                                                   
#   3. Slice out the middle four numbers into middle and print that slice.                                                                                                                                 
#   4. Build even_squares = [n * n for n in nums if n % 2 == 0] and print both lists.                                                                                                                      
#   5. Pop the first and last items from the original list, store them together (tuple/list), and print the removed pair plus what remains.                                                                
#   6. Compute the average of the remaining numbers and print Average: xx.xx.          

nums =[23,45,343,5,677,66,55,444]
numsm=nums[2:6]

for idx,n in enumerate(nums):
    print(str(idx).zfill(2) ,n)

print(numsm)

even_squares=[n * n for n in nums if n%2==0]
print(even_squares)

even_squares=[n * n for n in numsm if n%2==0]
print(even_squares)

poped=[nums.pop(0),nums.pop(-1)]
print(poped)
print(nums)

avg=sum(nums)/len(nums)
print(f"the avg is: {avg:.2f}")