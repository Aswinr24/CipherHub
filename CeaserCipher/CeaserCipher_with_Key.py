# The string to be encrypted/decrypted:
message = input()
# The encryption/decryption key:
key = int(input("Enter the key:"))
# Whether the program encrypts or decrypts:
mode = 'encrypt' # Set to either 'encrypt' or 'decrypt'
set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
translated = ''
for text in message:
  if text in set:
    textIndex = set.find(text)
    if mode == 'encrypt':
     translatedtext = textIndex + key
    elif mode == 'decrypt':
     translatedtext = textIndex - key
     
    if translatedtext >= len(set):
      translatedtext = translatedtext - len(set)
    elif translatedtext < 0:
      translatedtext = translatedtext + len(set)
    translated = translated + set[translatedtext]
  else:
    translated = translated + text
print(translated)
