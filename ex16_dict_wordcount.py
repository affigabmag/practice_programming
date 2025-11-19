#   New Practices                                                                                                                                                                                                                               
                                                                                                                                                                                                                                              
#   - ex16_dict_wordcount.py: store a short paragraph in a string, split it into words, and build a dictionary counting occurrences (normalize case, strip punctuation). Print the dictionary, then list the three most common words. Bonus:    
#     accept an input word and report its frequency via dict.get(...).                                                                                                                                                                          
#   - ex17_dict_merge_compare.py: create two inventory dictionaries (e.g., warehouse_a, warehouse_b). Merge them into combined where counts add when the same SKU appears in both. Print SKUs that exist only in one warehouse, then find the   
#     SKU with the largest combined count. Bonus: output a sorted list of (sku, count) tuples descending by count.
                                                                                                                                                                                                                                              
#   Try implementing each in new files so they sit alongside ex11–ex15. Natural next steps: run each script to verify the outputs, then tweak the data (e.g., add more SKUs or words) to explore edge cases.     

# › steps onl;y for 16                                                                                                                                                                                                                          
                                                                                                                                                                                                                                              

# • - Define a multi-sentence paragraph string.
#   - Convert to lowercase, strip punctuation, and split into words.                                                                                                                                                                            
#   - Use a dictionary to count each word’s occurrences.                                                                                                                                                                                        
#   - Print the entire dictionary.                                                                                                                                                                                                              
#   - Sort by count and display the top three words.                                                                                                                                                                                            
#   - Prompt for a word and report its count via dict.get.    

multistr="Hello this is a test. this is he 1st line.\r\n"
multistr+="I'm just entering here works for ex 16 that deals with wordcount exercise. this is the 2nd line\r\n"
multistr+="This is the 3rd line."

print (multistr)
print(multistr.lower())
multistr= multistr.replace(".","")
multistr= multistr.replace("'","")
multistr= multistr.replace("\r\n"," ")
multistr= multistr.replace("?","")
print(multistr)

words=multistr.split()
print(words)

words_count={}

#   - Use a dictionary to count each word’s occurrences.                                                                                                                                                                                        
for word in words:
    print(word,multistr.count(word))
    words_count[word]=multistr.count(word)

#   - Print the entire dictionary.                                                                                                                                                                                                              
print(words_count)
for key,value in words_count.items():
    print(key,value)
    
#   - Sort by count and display the top three words.                                                                                                                                                                                            
sorted_dict = dict(sorted(words_count.items(), key=lambda item: item[1],reverse=True)[:3])
print("\r\nsorted: ",sorted_dict)

#   - Prompt for a word and report its count via dict.get.    
word2search=input("Enter a word to search it's occurances: ")
count=words_count.get(word2search,0)
print(f"{word2search} appears {count} times")
