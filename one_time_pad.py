import random
from pickling import put

def enc(text):
    text = text.upper()
    letter = ["A","B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y',"Z"]
    value = []
    for i in range(26):
        value.append(i)

    cipher = ""
    key = ""
    for i in range(0,len(text)):
        if text[i] == " ":
            key += " "
        else:
            key += random.choice(letter)

    for i in range(0,len(text)):
        try:
            val = value[letter.index(text[i])] + value[letter.index(key[i])]
            if val > 25:
                val = val-26
            cipher += letter[val]
        except ValueError:
            cipher += " "
            continue

    a = put(cipher, key)

    return cipher, key
        

def dec(cipher, key):
    letter = ["A","B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y',"Z"]
    value = []
    for i in range(26):
        value.append(i)
    text = ""

    for i in range(0,len(cipher)):
        try:
            val = value[letter.index(cipher[i])] - value[letter.index(key[i])]
            if val < 0:
                val = val + 26
            text += letter[val]
        except ValueError:
            text += " "
            continue

    return text
        
    

        
    


    
