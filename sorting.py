import pandas as pd
import matplotlib.pyplot as plt


covid = pd.read_csv('dataset analysis/italy-covid-daywise.csv')

#print(covid.sort_values('new_cases',ascending=False).head(10))



#----------------------------------------------------------------------------------------------
covid['date'] = pd.to_datetime(covid.date)       #The dataType of date(column) previously was string, we changed the
                                                 # dataType into dateTime so we can individually access year,month etc,
                                                 # which can be used for sorting.
covid['year'] = pd.DatetimeIndex(covid.date).year
covid['month'] = pd.DatetimeIndex(covid.date).month
covid['day'] = pd.DatetimeIndex(covid.date).day
covid['weekday'] = pd.DatetimeIndex(covid.date).weekday
#print(covid)

#----------------------------------------------------------------------------------------------

# Question:
# Find out the number of tests,deaths,new_cases done in march.


#print(covid[covid.month == 3][['new_cases', 'new_deaths', 'new_tests']].sum())

#----------------------------------------------------------------------------------------------
# Question;
# Find the monthly total of tests,deaths,new_cases.


covid_monthly_df = covid.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()
# print(covid_monthly_df)
#----------------------------------------------------------------------------------------------
# Question;
# Find the cummulative sum of new_cases.


covid['total_cases'] = covid.new_cases.cumsum()
#print(covid)
#----------------------------------------------------------------------------------------------
# Saving it the CSV File.

covid.to_csv('Processored_data')
#----------------------------------------------------------------------------------------------

# Plot :

# covid.new_cases.plot()
# plt.show()

#----------------------------------------------------------------------------------------------
# Comparison Graphs:

# covid.new_cases.plot()
# covid.new_deaths.plot()
# plt.show()

#----------------------------------------------------------------------------------------------
# Death Rate Graph:

covid['total_deaths'] = covid.new_deaths.cumsum()
# print(covid)

# death_rate = covid.total_deaths / covid.total_cases
# death_rate.plot(title='Death Rate')
# plt.show()

#----------------------------------------------------------------------------------------------
# Positive Rate Graph:

covid['total_tests'] = covid.new_tests.cumsum()
print(covid)

positive_rate = covid.new_cases /  covid.new_tests
positive_rate.plot(title='Positive Rate')
plt.show()

#----------------------------------------------------------------------------------------------
# Bar Graph:

covid.new_tests.plot(kind='bar')
# plt.show()