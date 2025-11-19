#   - Create products dict with ≥6 items/prices.                                                                                                                                                                           
#   - Use a dict comprehension to build premium = {item: price for item, price in products.items() if price >= 50}.                                                                                                        
#   - Print both dicts and the count of premium items.              

products={
    'apple':4.5,
    'pc':54.35,
    'smartphone':664.65,
    'speaker':4775.566,
    'laptop':4665.566,
    'pineapple':444.55,
    'melon':894.58,
}

premium={item: price for item, price in products.items() if price>=50}

print("All products:", products)
print("Premium products:", premium)
print("Premium count:", len(premium))
