# def calculate_love_score(a, b):
#     total1=0
#     total2=0
#     for i in a.upper():
#         if i in "TRUE":
#             total1+=1
#     for j in b.upper():
#         if j in "TRUE":
#             total2+=1
#     total3 = total1 +total2


#     total4 = 0
#     total5 = 0
#     for k in a.upper():
#         if k in "LOVE":
#             total4+=1
#     for l in b.upper():
#         if l in "LOVE":
#             total5+=1
#     total6 = total4 +total5
#     print(str(total3)+ str(total6))
# calculate_love_score("Makanan sya","TesTesaja")

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Pepaya", "Menari")
