ex_list = [44, 34, 56, 27, 101, 68, 3, 46, 170, 97]

def find_max(list):
    max = list[0]
    for num in list:
        if num > max:
            max = num
            
    return max
        
print(find_max(ex_list))