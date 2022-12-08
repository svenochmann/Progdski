"""Aufgabe 2"""
"""Imports"""
import pandas as pd

"""Imort Data"""

df1 = pd.DataFrame({
    'id':[101,107,133,204,304],
    'Name': ['Alex', 'Amy', 'Allen', 'Bran', 'Betty'],
    'subject_1_score':[8.2, 6.0, 8.8, 4.5, 7.5]})

df2 = pd.DataFrame({
    'id':[101,107,204,634,304],
    'Name': ['Alex', 'Amy', 'Bran', 'Bryce', 'Betty'],
    'subject_2_score':[8.6, 5.0, 9.2, 6.8, 6.2]})


"""Merge Data"""
full_data = pd.merge_ordered(df1, df2)
full_data = full_data.set_index("Name")



"""Code"""
for student_name in full_data.index:
    print("\n" + student_name)
    mean_score = full_data.loc[student_name]['subject_1_score':].mean()
    
    print(f"Mean score: {mean_score}")        
    
    missing_scores=full_data.loc[student_name]['subject_1_score':].mean(skipna=False)
    try:
        missing_scores is int(missing_scores)
        missing_scores ="False"
    except:
        missing_scores="True"
    
    print(f"Missing scores?: {missing_scores}")
    



"""Beispiel Ausgabe
Alex
Mean score: 8.399999999999999
Missing scores?: False
Amy
Mean score: 5.5
Missing scores?: False
Allen
Mean score: 8.8
Missing scores?: True
Bran
Mean score: 6.85
Missing scores?: False
Betty
Mean score: 6.85
Missing scores?: False
Bryce
Mean score: 6.8
Missing scores?: True
"""
