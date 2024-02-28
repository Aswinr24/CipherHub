key=input()
ciphertext=input()
decrypted = ""
key_length = len(key)
index = 0
for text in ciphertext:
    if text.isalpha():
        if text.islower():
            decrypted += chr((ord(text) - ord(key[index].lower()) + 26) % 26 + ord('a'))
        elif text.isupper():
            decrypted += chr((ord(text) - ord(key[index].upper()) + 26) % 26 + ord('A'))
        index = (index + 1) % key_length
    else:
        decrypted += text
print(f'{decrypted}')
