


def caesar_encode(text, shift, alphabet="abcdefghijklmnopqrstuvwxyz .,!?äöü"):
    encrypt_text =""
    i = 0
    for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift
                if new_position >33:
                    """
                        Checks if the position is out of range 
                        and if so it counts back from the beginning
                        than saves it to my encrypt text
                    """
                    new_position_2 = new_position-34
        
                    new_letter_2 = alphabet[new_position_2]
            
                    encrypt_text += new_letter_2
                else:
                    new_letter_1 = alphabet[new_position]
                    encrypt_text += new_letter_1
            else:
                encrypt_text += letter
                pass    
    return encrypt_text #  =>Gives back the new and encrypted text

encrypted_text = "k j?xebmj.btxww,nbvjwbxqwnby xp jvvbtj!vbn j,nwc"


for i in range(32):
    """
        it runs 32 times and checks each shift, for 32 runs
        to find the right shift
    """
    print(caesar_encode(encrypted_text, i))
"""
    Das ergebnis lauted:
    "bravo! das konnte man ohne programm kaum eraten."
    
"""
