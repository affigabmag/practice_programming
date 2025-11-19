#   Exercise 7 - Lists
#   Start with any list of integers. Use a list comprehension to build a new list containing the
#   squares of only the even numbers from the original list, then print both lists.

nums = [12, 3453, 676, 5, 565, 44, 334, 23, 45, 4]

squares = [n * n for n in nums if n % 2 == 0]
print(nums)
print(squares)

