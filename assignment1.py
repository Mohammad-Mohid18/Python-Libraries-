import pandas as pd

weather_data =  pd.read_csv('Lecture/Weather_Data.csv')
#print(weather_data)

#print(weather_data.isnull().sum())

#print(weather_data.describe())

# print(weather_data.info())

print('mean  ')
print(weather_data.mean(numeric_only=True))
print('median ')
print(weather_data.median(numeric_only=True))
print('mode ')
print(weather_data.mode().iloc[0])
print('standard deviation ')
print(weather_data.std(numeric_only=True))
print('variance ')
print(weather_data.var(numeric_only=True))
print('Correlation ')
print(weather_data.corr(numeric_only=True))