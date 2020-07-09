# Program to predict admission chances

import pandas as pd

# unpickle model
model = pd.read_pickle('LR_model.pickle')

prompts = ['GRE','TOEFL','CGPA']
data = []
for p in prompts:
    data.append( input('Enter ' + p + ' : '))

# convert all values to float
for idx,value in enumerate (data):
    data[idx] = float(value)    

   
result = model.predict([data])
print(f"Probability of getting admission is : {result[0]*100}% ")