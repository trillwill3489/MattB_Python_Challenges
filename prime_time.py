original_num = int(input("Enter number to check if prime: "))

def prime_checker(a):
    
    multiple_list = []

    a = original_num
  
    while a > 2:
        a -= 1
        multiple_list.append(a)

    for x in multiple_list:
        if original_num % x == 0:
            return False
        else:
            pass
    
    return True
print(prime_checker(original_num))