


def caesar_encode(text, shift, alphabet="abcdefghijklmnopqrstuvwxyz .,!?äöü"):
    encrypt_text =""
    for letter in text:    
        if letter in alphabet:
             """Es Checkt ob letter im alphabet ist"""
             position = alphabet.index(letter)
        else:
            position = " "

        new_position = position + shift
        if new_position >32:
            new_position_2 = new_position-33
            
            new_letter_2 = alphabet[new_position_2]
            
            encrypt_text += new_letter_2
        else:
            new_letter_1 = alphabet[new_position]
            encrypt_text += new_letter_1
    return encrypt_text


    