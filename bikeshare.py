import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#defining variables___________________________________________________________
cities = ['chicago','new york city', 'washington','all']
months=['januray','february','march','april','may','june','all']
days=['sunday','monday','tuesday','wednesday','thursday','friday','all']
#getting sepcified data for cities,months and days from user____________________________________________
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #cities_____________________________________________________________________________________________
    while True:
        city=input("choose a city name to explore or type all for all cities:").lower()
        if city in cities:
            break
        else:
            print("please choose a valid city name")
            print("you can choose a city from:(chicago,new york city,washington)or all for all cities as metnioned")
    #months_____________________________________________________________________________________________
    while True:
        month=input("choose a month from (januray,february,march,april,may,june)or all months:").lower()
        if month in months:
            break
        else:
            print("please choose a valid month")
    #days_____________________________________________________________________________________________
    while True:
        day=input("choose a day or type all for all days:").lower()
        if day in days:
            break
        else:
            print("please choose a valid day")
            
            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #____________________________________________________________________________
    df=pd.read_csv(CITY_DATA[city])
    # converting the Start Time column to datetime________________________________
    df['start_time']=pd.to_datetime(df['start_time'])
    #extracting month,day,hour to create a new column for each _______________________________________
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour']= df['start_time'].dt.hour
    #filter by month_____________________
    if month != 'all':
        #use the index of the months list to get the corresponding int
        months=['januray','february','march','april','may','june']
        months=months.index(month)+ 1
        #filter by month to create new dataframe
        df=df[df['month']==month.lower()]
        #filter by day 
    if day != 'all':
        df=df[df['day']==day.lower()]
    
    return df

