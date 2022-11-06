"""Aufgabe 4.1"""


def caesar_encode(text, shift, alphabet="abcdefghijklmnopqrstuvwxyz"):
    encrypt_text =""
    
    for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift
                if new_position >25:
                    """
                        Checks if the position is out of range 
                        and if so it counts back from the beginning
                        than saves it to my encrypt text
                    """
                    new_position_2 = new_position-26
        
                    new_letter_2 = alphabet[new_position_2]
            
                    encrypt_text += new_letter_2
                else:
                    new_letter_1 = alphabet[new_position]
                    encrypt_text += new_letter_1
            else:
                encrypt_text += letter
                pass    
    return encrypt_text #  =>Gives back the new and encrypted text





"""Beispiel Output"""

print(caesar_encode("mein text!", shift=15))
    # => btxc itmi!
