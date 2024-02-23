message=input()
decrypted = ""
    for text in message:
        if text.isalpha():
            if text.islower():
                decrypted += chr(ord('z') - (ord(text) - ord('a')))
            elif text.isupper():
                decrypted += chr(ord('Z') - (ord(text) - ord('A')))
        else:
            decrypted += text
    print(decrypted)
