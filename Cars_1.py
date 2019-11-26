import pandas as pd
#loads the file 'cars.csv'
cars = pd.read_csv('cars.csv')
#Get the first five rows of the resulting cars
x = cars.head()
#Get the last five rows of the resulting cars
y = cars.tail()
#Combine the rows by appending
z = x.append(y)
#Print the Cars included
print(z)