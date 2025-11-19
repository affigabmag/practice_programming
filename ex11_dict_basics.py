#   Create a new file named ex11_dict_basics.py and do the following:                                                                                                                                      
#   1. Make a dictionary called person with at least four key/value pairs (e.g., name, age, city, hobby).                                                                                                  
#   2. Print the entire dictionary.                                                                                                                                                                        
#   3. Print only the keys, then only the values (use person.keys() / person.values() or convert them to lists).                                                                                           
#   4. Add a new key/value pair (e.g., "email": "example@domain.com") and print the dictionary again to show the update.     

person={ 'name':'gabi','age':53,'city':'beer sheva','hobby':'music'}
print(person)
print(person.keys())
print(person.values())
person["email"]="a@b.com"
print(person)
print(person.keys())
print(person.values())