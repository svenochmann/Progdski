
#Results of the dice
results_dice = [1, 5, 5, 2, 6, 2, 4, 2, 3, 6, 1, 2, 1, 6, 4, 5, 1, 1, 2, 6]

#region Task 1.1

#Counts how often the number 1 gets diced and
#saves the count number in count_of_1
count_of_1 = results_dice.count(1)

#prints the amount
print(f"Die Eins wurde {count_of_1} mal gewürfelt.")

#endregion



#region Task 1.2

#checks on what index the 3 appears the first time and
#saves the index number in count_to_3
count_to_3 = results_dice.index(3)

#Add +1 to my result bc index starts at 0
count_to_3 = count_to_3+1
#Prints the Amount
print(f"Die Drei wurde nach {count_to_3} Versuchen gewürfelt.")


#endregion
