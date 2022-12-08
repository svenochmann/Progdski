#funktion to multiply the 2 largest numbers in a list
#funktion returns 3 results: [0] the Result, [1] number_1, [2]number_2
def multiply_two_largest(number):
    #sort list numbers
    number.sort()
    
    #saves larest number in number_1
    number_1 = number[-1]
    
    #saves second largest number in number_2
    number_2 = number[-2]
    
    # Multiplys both numbers
    result = number_1 * number_2
    
    #returns 3 numbers
    return result, number_1, number_2

#uses the funktion with example list => 20
result_funktion = multiply_two_largest([1, 2, 3, 4, 5, 1])  # => 20


#prints the Result:[0] the Result, [1] number_1, [2]number_2
#
print(f"{result_funktion[1]} * {result_funktion[2]} = {result_funktion[0]}")