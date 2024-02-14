message = input()
mode = 'encrypt' # Set to either 'encrypt' or 'decrypt'
set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
translatedText = ''
for key in range(len(set)): 
 translatedText = ''
 for text in message:
  if text in set:
   textIndex = set.find(text)
   translatedIndex = textIndex - key
   if translatedIndex < 0:
     translatedIndex = translatedIndex + len(set)
   translatedText = translatedText + set[translatedIndex]
  else:
   translatedText = translatedText + text

#Displays all possible encryptions
 print('Key ',key,': ',translatedText)
