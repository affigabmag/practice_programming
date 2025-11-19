#   On to Exercise 12 (Dictionaries): create a file ex12_dict_lookup.py that:
                                                                                                                                                                                                         
#   1. Defines a dictionary mapping three country codes (like "IL", "US", "FR") to their capital cities.                                                                                                   
#   2. Prompts the user for a code (or you can hardcode one for now) and prints the capital if the key exists.                                                                                             
#   3. If the code isn’t found, print something like “Code not recognized”.   

capitals={
    'il':'jerusalem',
    'us':'washington dc',
    'fr':'paris'
}

code=input("enter country code:").lower()

print(capitals.get(code,"Code not recognized"))
