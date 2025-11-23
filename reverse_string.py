word = input("Enter some word: ")

def reverse_string(some_str):
    new_str = some_str[::-1]
    return new_str

print(f"{word} turned backwards is {reverse_string(word)}")