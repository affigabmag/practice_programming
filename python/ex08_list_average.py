#   Exercise 8 – Lists                                                                              
#   Create a list of five floating-point numbers. Calculate their average (sum divided by count) and
#   print a formatted string like Average: 12.34. (Use f-strings or format.)  

floats=[12.4,78.565,343.445,33.454,55.55]
avg=sum(floats)/len(floats)
print(f"Average: {avg:.2f}")
