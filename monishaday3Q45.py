import pandas as pd

df = pd.read_csv('Automobile_data.csv')
#print(df[['make']]['make'].value_counts().to_frame('count'))

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
 # create dataframe from dict here
carsDf1 = pd.DataFrame.from_dict(GermanCars)
#print(carsDf1)

japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
carsDf2 = pd.DataFrame.from_dict(japaneseCars)
#print(carsDf2)
#
# carsDf = # Write your code to concatenate here
carsDf = pd.concat([carsDf1,carsDf2],keys = ['Germancars','japanesecars'])
print(carsDf)

#carsDf

