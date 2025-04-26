import pandas as pd

covid_data = pd.read_csv('dataset analysis/italy-covid-daywise.csv')
#print(covid_data)

#print(covid_data['new_cases'])

#print(type(covid_data['new_cases']))

# print(covid_data['new_cases'][239])
# print(covid_data['new_tests'][240])

# print(covid_data.at[240,'new_tests'])
# print(covid_data.at[236,'date'])

# covid_copy = (covid_data.copy())
# print(covid_copy)

# print(covid_data.loc[243])
# print(covid_data.loc[100:108])

# print(covid_data.head(7))  #similar for the tail.

# print(covid_data.new_tests.first_valid_index())

print(covid_data.sample(15))