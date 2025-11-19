#   Exercise 5 – Lists                                                                              
#   Create two lists of equal length. Combine them into a single list using concatenation (not a    
#   loop), then print the combined list and its total length.  

nums1=[123,565,3334,87,334]
nums2=[345,676,33,3,22]

# nums1+=nums2
nums1.extend(nums2)
print(nums1)

