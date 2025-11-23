word = input("Enter a phrase, our function will check if it is a palindrome: ")

def is_palindrome(word):
    str_check = word.lower()
    str_check = str_check.replace(" ", "")
    
    if str_check == str_check[::-1]:
        return print(f"{word} is a palindrome")
    else:
        return print(f"{word} is not a palindrome")

is_palindrome(word)