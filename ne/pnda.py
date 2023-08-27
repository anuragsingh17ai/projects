import pandas as pd
# # for series
# a=[1,2,3,4]
# print(pd.Series(a))
# print(pd.Series(a,index=['v','x','y','z']))

# #for dictionary
# calories={'day1':420,'day2':380,'day3':390}
# print(pd.Series(calories))
# print(pd.Series(calories,index=['day1','day2']))

###### Two dimension data structure
# data={
#     'calories':[22,33,44],
#     'duration':[3,4,5]
# }
# print(pd.DataFrame(data))
#print(pd.DataFrame(data).loc[0])
#print(pd.DataFrame(data).loc[[0,2]])
# print(pd.DataFrame(data,index=['data1','data2','data3']).loc[['data1','data3']])

###csv file
# print(pd.read_csv('data.csv'))
# print(pd.read_csv('data.csv').to_string())

#json file
# print(pd.read_json('data1.json'))
# print(pd.read_json('data1.json').to_string())
# print(pd.read_csv('data.csv').head())
# print(pd.read_csv('data.csv').head(10))
#print(pd.read_csv('data.csv').tail())
# print(pd.read_csv('data.csv').tail(3))

# print(pd.read_csv('data.csv').info())
# print(pd.read_csv('data.csv').dropna().info())
# print(pd.read_csv('data.csv').dropna())
# print(pd.read_csv('data.csv').fillna(130,inplace=True))

df=pd.read_csv('data.csv')
# print(df['Calories'].mean())
# print(df['Calories'].median())
print(df['Calories'].mode())