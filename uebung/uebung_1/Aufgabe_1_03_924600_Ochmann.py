#funktion sorts the list ascending and
#returns requested position(nth)
#nth = 1 = smallest number in list, etc  
def nth_smallest(numbers, nth):
    
        #removes duplicates in [numbers]
        numbers = list(set(numbers))
        # Sorts [numbers] ascending
        numbers.sort()
        #condition checks if the requeste position exists
        if nth <= len(numbers):
            #Takes the requestet spot out of [nummbers] based on the Index
            #[nth-1] bc the Index starts at 0 not 1
            result = numbers[nth-1]
        else: #when requested position in list is not available it gives out "None" 
            result = "None"
        return result

# print of the task examples
print(nth_smallest([4,4,6,5,1,2,1], 1))          # => 1
print(nth_smallest([4,4,6,5,1,2,1], 3))          # => 4
print(nth_smallest([3,5,3,3,3,5], 3))            # => None
