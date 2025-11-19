# Create two lists of equal length (your choice of values). 
# Combine them into a single list using concatenation (e.g., combined = list1 + list2 or list1.extend(list2)). 
# Print the combined list and its total length. 
# Then, split the combined list back into two halves and print the halves to show they match the originals. 
# Save as ex05b.py and let me know when it’s ready.   

nums1=[122,232,3,33,4]
nums2=[22,346,445,45,4]
combined=nums1+nums2
print(combined)
print(f"total length is: {len(combined)}")
half=int(len(combined)/2)
half1=combined[:half]
half2=combined[half:]
print(half)
print(half1)
print(half2)
