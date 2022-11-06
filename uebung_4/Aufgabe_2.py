

def caesar_encode(text, shift, alphabet="abcdefghijklmnopqrstuvwxyz"):
    encrypt_text =""
    for letter in text:
            
        
        position = alphabet.index(letter)
        
        new_position = position + shift
        if new_position >25:
            new_position_2 = new_position-26
            
            new_letter_2 = alphabet[new_position_2]
            
            encrypt_text += new_letter_2
        else:
            new_letter_1 = alphabet[new_position]
            encrypt_text += new_letter_1
    return encrypt_text

encrypted_text= "xri eztyk jtycvtyk wlvi uve rewrex."

for i in range(25):
    """
        it runs 25 times and checks each shift, for 25 runs
        to find the right shift
    """
    print(caesar_encode(encrypted_text, i))


    