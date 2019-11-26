import pandas as pd
#loads the file 'cars.csv'
cars = pd.read_csv('cars.csv')
# a.) Display the first five rows with odd numbered columns.
a = cars.iloc[0:5, 0::2]
print(a)
print(" ")
# b.) Display the row that contains the "Model" of Masda RX4.
b = cars.iloc[0:1]
print(b)
print("")
# c.) How many cylinders does the car model"Camaro Z26" have?
c = cars.loc[[23],["Model","cyl"]]
print(c)
print("")
# d.) Determine how many cylinders and what gear type do the car models Mazda RX4 Wag, Ford Pantera L , and Honda Civic have.
d = cars.loc[[1,28,18],["Model","cyl","gear"]]
print(d)