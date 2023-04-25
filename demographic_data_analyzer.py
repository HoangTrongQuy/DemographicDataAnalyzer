import pandas as pd
from tensorboard import data

data = pd.read_csv('adult.data.csv')

# print(data.info())
data_race = data['race'].value_counts()
# print(data_race)

data_age_men = round(data[data['sex'] == 'Male']['age'].mean(),1)
# print(data_age_men)

data_education = data['education'].value_counts()
# print(data_education)
d = data.shape[0]
# print(d)
# print(data_education['Bachelors'])
# print(round(data_education['Bachelors']/d,1))
print("-----------------------")
d1 = data[data['education'] == 'Bachelors']['education'].count()
d2 = data['education'].count()
# print(round(d1/d,1))

data_salary_1 = data[(data['education'] == 'Bachelors') | (data['education']=='Masters')
                   | (data['education']=='Doctorate')]
data_salary_2 = data[((data['education'] == 'Bachelors') | (data['education']=='Masters')
                   | (data['education']=='Doctorate')) & (data['salary'] != '<=50K')]

total_salary_1 = data_salary_1.shape[0]
total_salary_2 = data_salary_2.shape[0]
# print(round(total_salary_2/total_salary_1 * 100,1))

data_salary_3 = data[(~((data['education'] == 'Bachelors') | (data['education']=='Masters')
                   | (data['education']=='Doctorate'))) & (data['salary'] == '>50K')]
# print(round(data_salary_3.shape[0]/(d-total_salary_1) * 100, 1))

data_hours = data['hours-per-week'].min()
# print(data_hours)

data_people_min_1 = data[((data['hours-per-week']==data_hours))].shape[0]
data_people_min_2 = data[((data['hours-per-week']==data_hours) & (data['salary'] == '>50K'))].shape[0]
# print(round(data_people_min_2/ data_people_min_1 * 100,1))

data_countries = data[data['salary'] == '>50K']['native-country'].value_counts(ascending= False)
# print(data_countries)
total_people = data.groupby(['native-country'])['native-country'].count()
percentage_people = round(data_countries/total_people * 100,1)
# print(percentage_people)
hightest_country = percentage_people.idxmax()
# print(hightest_country)
hightest_percentage = percentage_people.max()
# print(hightest_percentage)

data_occupation = data[(data['native-country'] == 'India') & (data['salary']=='>50K')]['occupation'].value_counts()
# print(data_occupation.index[0])

print('How many people of each race are represented in this dataset?')
print(data_race)
print("-----------------------")

print('What is the average age of men ?')
print(data_age_men)
print("-----------------------")

print("What is the percentage of people who have a Bachelor's degree?")
print(round(d1/d,1))
print("-----------------------")

print("What percenteage of people with advanced education(Bachelors, Masters, or Doctorate) make more than 60K?")
print(round(total_salary_2/total_salary_1 * 100,1))
print("-----------------------")

print('What percentage of people without advanced education make more than 50K?')
print(round(data_salary_3.shape[0]/(d-total_salary_1) * 100, 1))
print("-----------------------")

print('What country has the highest percentage of people that earn >50K and what is that percentage?')
print("the hightest percentage:", hightest_country)
print("Percentage:", hightest_percentage)
print("-----------------------")

print('Identify the most popular occupation for those who earn >50K in India.')
print(data_occupation.index[0])