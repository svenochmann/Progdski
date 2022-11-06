


def caesar_encode(text, shift, alphabet="abcdefghijklmnopqrstuvwxyz .,!?äöü"):
    encrypt_text =""
    for letter in text:    
        
        position = alphabet.index(letter)
        
        
        new_position = position + shift

        if new_position >32:
            new_position_2 = new_position-33
            
            new_letter_2 = alphabet[new_position_2]
            
            encrypt_text += new_letter_2
        else:
            new_letter_1 = alphabet[new_position]
            encrypt_text += new_letter_1
    return encrypt_text

encrypted_text = "k j?xebmj.btxww,nbvjwbxqwnby xp jvvbtj!vbn j,nwc"


for i in range(32):
    """
        it runs 32 times and checks each shift, for 32 runs
        to find the right shift
    """
    print(caesar_encode(encrypted_text, i))
