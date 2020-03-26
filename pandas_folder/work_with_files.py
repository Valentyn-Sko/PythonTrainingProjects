import os

import pandas

print(os.listdir('files/'))

df1 = pandas.read_csv('files/original.csv')
print(df1)

df2 = pandas.read_json('files/supermarket.json')
print(df2)

df3 = pandas.read_excel('files/original.xlsx')
print(df3)

print("txt with ,")
df4 = pandas.read_csv('files/supermarket_with_comas.txt', sep=',')
print(df4)

print("txt with ;")
df4 = pandas.read_csv('files/supermarket_with_semi.txt', sep=';')
print(df4)

df6 = df4.drop(df4.columns[0:3],1)
print(df6)

df5 = df4.set_index("Address")
df5.drop("332 Hill St", 0)
print(df5)

df5["Continent"] = df5.shape[0]*["North America"] # new column
print(df5)


df5['SomeCol'] = df5["Country"]+"Some"
print(df5)

df5_t= df5.T # change x and y 
print(df5_t)