# This are the links that i used to take help for solving the below project.
# https://www.python-course.eu/python3_input.php
# https://peps.python.org/pep-0257/
# https://github.com/beingjainparas/Udacity-Explore_US_Bikeshare_Data/blob/master/bikeshare_2.py#L210

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    cities = ['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
   print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
while True:
        city = input("Enter city (chicago, new york city, washington): ").lower()
        if city in cities:
            break
        else:
    print("Invalid input. Please choose from chicago, new york city, or washington.")

    # TO DO: get user input for month (all, january, february, ... , june)
   while True:
        month = input("Enter month (january, february, march, april, may, june, all): ").lower()
        if month in months:
            break
        else:
   print("Invalid input. Please choose from january, february, march, april, may, june, all.")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
   while True:
        day = input("Enter day of week (monday, tuesday, wednesday, thursday, friday, saturday, sunday, all): ").lower()
        if day in days:
            break
        else:
    print("Invalid input. Please choose from monday, tuesday, wednesday, thursday, friday, saturday, sunday, all.")

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
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour()
    
    if month != 'all':
        df = df[df['month'] == month.title()]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]    
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month: " + most_common_month)
    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is: " + common_day_of_week)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The most Common Start Hour: " + popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station from the given fitered data is: " + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station from the given fitered data is: " + common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_combo'] = df['Start Station'] + " to " + df['End Station']
    most_common_trip = df['start_end_combo'].mode()[0]
    print("The most frequent combination of start and end station trip: " + most_common_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time from the given fitered data is: " + str(total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time from the given fitered data is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types from the given fitered data is: \n" + str(user_types))

    # TO DO: Display counts of gender
      if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
    print("Counts of gender:\n", gender_counts)
      else:
    print("Gender data is not available for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
      if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
    print(f"Earliest year of birth: {earliest_year}")
    print(f"Most recent year of birth: {most_recent_year}")
    print(f"Most common year of birth: {most_common_year}")
    else:
    print("Birth year data is not available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
          
def display_raw_data(df):
    """Displays raw data on user request.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
   
     view_raw_data = input("\nWould you like to see raw data? Type 'yes' or 'no': ").lower()
      if view_raw_data == 'yes':
          start_loc = 0
         while True:
    print(df.iloc[start_loc:start_loc+5])  # Show 5 rows at a time
           start_loc += 5
           more = input("Do you want to see more? Type 'yes' or 'no': ").lower()
       if more != 'yes':
                    break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
          

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
