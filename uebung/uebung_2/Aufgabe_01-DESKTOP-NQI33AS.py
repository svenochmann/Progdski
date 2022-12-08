"""
    Quiz: 
        Antwort: b
"""


"""
    Aufgabe 01
"""




def war_of_numbers(numbers):
    
    def is_even(number):
        if number % 2==0:
            return True #is even     
        else:
            return False#is odd
    
    
    print(len(numbers))
    i=0
    total=len(numbers)
    print(total)
    for _ in range(total):
        if is_even(numbers[i]) is True:
            number_even=[numbers[i]]
            i=i+1
        else:
            number_odd=[numbers[i]]
            i=i+1 
   
    sum_even =sum(number_even)
    sum_odd = sum(number_odd)
    
    
    if sum_even < sum_odd:
        print("Odd numbers win by margin of {sum_diff}!")
    elif sum_even > sum_odd:
        print("Even numbers win by margin of {sum_diff}!")
    else:
        print("The sums are equal: There is no winner!")
    
    









# Ausgabe

war_of_numbers([4, 5, 6, 9])     #=> Odd numbers win by margin of 4!
#war_of_numbers([4, 5, 6, 9, 10]) #=> Even numbers win by margin of 6!
#war_of_numbers([3, 3, 4, 2])     # => The sums are equal: There is no winner!
