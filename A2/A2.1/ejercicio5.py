list_num = [6, 9, 6, 9]
list_no_dupli = []  

for num in list_num:
    if num not in list_no_dupli:
        list_no_dupli.append(num)

print(list_no_dupli)
