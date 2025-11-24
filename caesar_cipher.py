original = input("Enter the phrase you would like to cipher out: ")
shift = int(input("What shift would you like?: "))

def caesar_encrypt(text, shift):

    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


ciphered = caesar_encrypt(original, shift)

print(f"{original} was ciphered into: {ciphered}")