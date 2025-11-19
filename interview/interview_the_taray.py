# from the thetarey
# =================
# algo o=n
# sort the array find the 
arry_sort = [1, 2, 6, 8, 9, 11, 23, 453]

def ret_id_fast(tgt):
    seen = {}  # ערך → אינדקס
    for i in range(len(arry_sort)):   # עוברים לפי אינדקס
        x = arry_sort[i]              # הערך במיקום i
        complement = tgt - x          # ההשלמה
        if complement in seen:
            return f"indices for target value {tgt} are {seen[complement]} and {i}"
        seen[x] = i                   # שמור את הערך והאינדקס שלו
    return "no pair found"

print(ret_id_fast(8))

# arry_sort=[1,2,6,8,9,11,23,453]

# def ret_id(tgt):
#     #print(arry_sort,tgt)
#     for x in arry_sort:
#         for y in arry_sort:
#             #print("\r\n",x,y)
#             if (x+y)==tgt:
#                 #print("values are: ",x,y)
#                 #print("indexs are: ",arry_sort.index(x) ,arry_sort.index(y))
#                 idx1=arry_sort.index(x)
#                 idx2=arry_sort.index(y)
#     return "indexs for target value "+str(tgt)+" are "+str(idx1)+" and "+str(idx2)

# print (ret_id(8))

# זה מוצא את האינדקסים של האיברים במערך שהסכום שלהם שווה לערך המטרה לדומגא 8

# זה עובד באלגוריתם של n  בחזקת 2.

# תן אךלגוריתם אחר של N 
