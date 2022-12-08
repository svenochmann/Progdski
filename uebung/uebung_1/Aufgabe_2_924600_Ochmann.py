"""
    Quiz: 
        Antwort: b
"""


"""
    Aufgabe 01
"""
def war_of_numbers(numbers):
    """
    

    Parameters
    ----------
    numbers : list of ints
        takes a list of integers.

    Returns
    -------
    None but prints
        Which won even or odd numbers in combination with the margin.

    """
    def is_even(number):
        """
        

        Parameters
        ----------
        number : int
            A number from the given list.

        Returns 
        -------
        Bool
            True when even and False when odd.

        """
        if number % 2==0:
            return True #is even     
        else:
            return False#is odd
    
    

    """
        Declaring:
            i : as index for the upcoming if condition.
            number_even : as list to save all even numbers.
            number_odd : as list to save all odd numbers.
            total : to save the lenght of our given list for readability.
    """
    i=0
    number_even=[]
    number_odd=[]
    
    
    
    total=len(numbers)
    for _ in range(total):
        """
            in this condition the programm takes the numbers 
            from our list
            and checks if there even or odd with our is_even funktion
        """
        if is_even(numbers[i]) is True:
            number_even.append(numbers[i])
            i=i+1
        else:
            number_odd.append(numbers[i])
            i=i+1 
   
    """
        takes the sum of our even numbers and our odd numbers and
        saves them in new variables for more readability
    """
    sum_even =sum(number_even)
    sum_odd = sum(number_odd)
    
    
    """
        in this if condition the program checks who won the odd or evn numbers
        and gives out the wining team and the margin by subtracting the numbers
    """
    
    if sum_even < sum_odd:
        sum_diff=sum_odd - sum_even
        print(f"Odd numbers win by margin of {sum_diff}!")
    elif sum_even > sum_odd:
        sum_diff=sum_even - sum_odd
        print(f"Even numbers win by margin of {sum_diff}!")
    else:
        print("The sums are equal: There is no winner!")
    
    





"""
    Test Ausgaben
"""
war_of_numbers([4, 5, 6, 9])     #=> Odd numbers win by margin of 4!
war_of_numbers([4, 5, 6, 9, 10]) #=> Even numbers win by margin of 6!
war_of_numbers([3, 3, 4, 2])     # => The sums are equal: There is no winner!
