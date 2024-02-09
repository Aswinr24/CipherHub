ciphertext=input()
i=len(ciphertext)-1
message=''
while i >= 0:
 message = message + ciphertext[i]
 i = i - 1
print(message)
