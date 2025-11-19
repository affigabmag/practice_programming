# • Exercise 15 (dictionaries + list slicing):
                                                                                                                                                                                                         
#   Create ex15_dict_filter.py that:                                                                                                                                                                       
                                                                                                                                                                                                         
#   1. Defines a dictionary prices with at least five items mapped to float prices (e.g., "apple": 1.2).                                                                                                   
#   2. Build a new dictionary expensive containing only the items that cost

# • Exercise 15 (dictionaries + list slicing):
#   Give it a shot and let me know when ex15_dict_filter.py is ready for review.

prices={
    'apple':1.2,
    'pineapple':4.5,
    'melon':5.4,
    'lemon':2.2,
    'grapfruit':14.3,
    'orange':1.4
}

expensive={}
for item,price in prices.items():
    if price>10:
        expensive[item]=price

print("All prices:", prices)
print("Expensive items:", expensive)
print("Count:", len(expensive))
