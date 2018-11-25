import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_CONVERT = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'july': 7,
    'august': 8,
    'september': 9,
    'october': 10,
    'november': 11,
    'december': 12,
    'all': 13}

DAY_CONVERT = {
    'monday': 1,
    'tuesday': 2,
    'wednesday': 3,
    'thursday': 4,
    'friday': 5,
    'saturday': 6,
    'sunday': 7,
    'all': 8
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('What city would you like to see the information for? ').lower()
    while city != "chicago" and city != "new york city" and city != "washington":
        print('\nThe city entered was incorrect.')
        city = input('What city would you like to see the information for? (Chicago, New York City, Washington)')

    # TO DO: get user input for month (all, january, february, ... , june)
    validMonths = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    month = input('What month would you like to see the information for? ' ).lower()
    while month not in validMonths:
        print('\nThe month entered is not correct.')
        month = input('What month would you like to see the information for? ' )


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    validDays = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day = input('What day of the week would you like to see information see? ').lower()
    while day not in validDays:
        print('\nThe day you entered is not valid. ')
        day = input('What day of the week would you like to see information see? ')

    print('-'*40)
    return city, month, day.capitalize()


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


    filename = CITY_DATA[city]
    df = pd.read_csv(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        int_month = MONTH_CONVERT[month]
        df['month'] = df['Start Time'].dt.month
        df = df[(df.month == int_month)]
    if day != 'all':
        df['day'] = df['Start Time'].dt.weekday_name
        df = df[(df.day == day)]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    # the most popular month
    popular_month = df['month'].mode()[0]
    print('Most popular Start Month: ', popular_month)

    # TO DO: display the most common day of week


    # the most popular day
    popular_day = df['day'].mode()[0]
    print('Most popular Start Day: ', popular_day)

    # TO DO: display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %.03f seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()
    print('The most common start station is: ', common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()
    print('The most common end station is: ', common_end)

    df['Start End'] = df['Start Station'].map(str) + '&' + df['End Station']
    common_both = df['Start End'].value_counts().idxmax()
    print('The most common combination of the start and end stations is: ',common_both)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total travel time is: ', total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('The average travel time is: ', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    # print value counts for each user type
    user_types = df['User Type'].value_counts()

    print(user_types)

    # TO DO: Display counts of gender
    if CITY_DATA != 'washington':
        gender = df['Gender'].value_counts()
    else:
        print ('Sorry this information is not available for Washington.')

    print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    birth_earliest = df['Birth Year'].min()
    print('The earliest birth year is: ', birth_earliest)

    birth_recent = df['Birth Year'].max()
    print('The most recent birth year is: ', birth_recent)

    birth_common = df['Birth Year'].mode()
    print('The most common birth year is: ', birth_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
