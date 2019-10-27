import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
# Initialization for input cities, months and days
cities = ['chicago', 'new york city', 'washington']
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
            try:
                city=input('Input your city between "chicago, new york city, washington": ').lower()
                if city in cities:
                    break
            except:
                print('Your input city is not between "chicago, new york city, washington" please true again')

    # Get user input for month (all, january, february, ... , june)
    while True:
            try:
                month=input('Input your month between "all, january, february, march, april, may, june": ').lower()
                if month in months:
                    break
            except:
                print('Your input month is not between "all, january, february, march, april, may, june" please true again')

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
            try:
                day=input('Input your day of week  between "all, sunday, monday, tuesday, wednesday, thursday, friday, saturday": ').lower()
                if day in days:
                    break
            except:
                print('Your Input day is not between all, sunday, monday, tuesday, wednesday, thursday, friday, saturday" please true again')


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
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.weekday_name

    # Filter by month
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        month = months.index(month) + 1
        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['Day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
        # extract month and day of week from Start Time to create new columns

    # Display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print("The most common month is : ", popular_month)

    # Display the most common day of week
    df['Day'] = df['Start Time'].dt.weekday_name
    popular_Day = df['Day'].mode()[0]
    print("The most common day of week is : ", popular_Day)

    # Display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] =df['Start Time'].dt.hour
    popular_hour =df['hour'].mode()[0]
    print("The most common start hour is : ", popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display commonly used start station by 5 rows
    x=0
    y=5
    aa =input('\nPlease input y if you want to see 5 row from Start Station\n And press any key to display most commonly used start station : ').lower()
    while aa=='y':
        try:
            for i in range(1):
                 start_station = df['Start Station'].iloc[x:y,]
                 print("The 5 row are in used start station : \n", start_station)
                 x+=5
                 y+=5
            print('----------------------------------')
            aa = input('\nWould you like to proceed? Enter y or no.\n')
            if aa.lower() != 'y':
                break
        except:
            print("You are finish all of rows : \n")
    print('----------------------------------')

    # Display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station : \n", start_station)
    print('----------------------------------')

    # Display commonly used end station by 5 rows
    x=0
    y=5
    bb=input('\nPlease input y if you want to see 5 row from End Station\n And press any key to display most commonly used end station: ').lower()
    while bb=='y':
        try:
            for i in range(1):
                 end_station = df['End Station'].iloc[x:y,]
                 print("The 5 row are in used end station : \n", end_station)
                 x+=5
                 y+=5
            print('----------------------------------')
            bb = input('\nWould you like to proceed? Enter y or no.\n')
            if bb.lower() != 'y':
                break
        except:
            print("You are finish all of rows : \n")
    print('----------------------------------')

    # Display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("\nThe most commonly used end station : \n", end_station)
    print('----------------------------------')

    # Display frequent combination of start station and end station trip by 5 rows
    x=0
    y=5
    cc =input('\nPlease input y if you want to see 5 row from Start End\n And press any key to display most frequent combination of start station and end station trip: ').lower()
    while cc=='y':
        try:
            for i in range(1):
                 df['Start End'] = df['Start Station'].map(str) + '&' + df['End Station']
                 popular_start_end = df['Start End'].iloc[x:y,]
                 print("The 5 row are in used start end station : \n", popular_start_end)
                 x+=5
                 y+=5
            print('----------------------------------')
            cc = input('\nWould you like to proceed? Enter y or no.\n')
            if cc.lower() != 'y':
                break
        except:
            print("You are finish all of rows : \n")
    print('----------------------------------')

    # Display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'].map(str) + '&' + df['End Station']
    popular_start_end = df['Start End'].value_counts().idxmax()
    print("\nThe most commonly used start station and end station : \n",popular_start_end)
    print('----------------------------------')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display Trip Duration by 5 rows
    x=0
    y=5
    dd =input('\nPlease input y if you want to see 5 row from Trip Duration\n And press any key to display total travel time: ').lower()
    while dd=='y':
        try:
            for i in range(1):
                 total_travel = df['Trip Duration'].iloc[x:y,]
                 print("The 5 row from Trip Duration : \n", total_travel)
                 x+=5
                 y+=5
            print('----------------------------------')
            dd = input('\nWould you like to proceed? Enter y or no.\n')
            if dd.lower() != 'y':
                break
        except:
            print("You are finish all of rows : \n")
    print('----------------------------------')

    # Display total travel time
    total_travel = np.sum(df['Trip Duration'])
    print("Total travel time : ", total_travel)

    # Display mean travel time
    mean_travel = np.mean(df['Trip Duration'])
    print("Mean travel time : ", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Counts of user types
    print(" *** Counts of user types : \n")

    # Display user types by 5 rows
    x=0
    y=5
    ee =input('\nPlease input y if you want to see 5 row from user types\n And press any key to display counts of user types : ').lower()
    while ee=='y':
        try:
            for i in range(1):
                 counts_of_user_types = df['User Type'].iloc[x:y,]
                 print("The 5 row from user types : \n", counts_of_user_types)
                 x+=5
                 y+=5
            print('----------------------------------')
            ee = input('\nWould you like to proceed? Enter y or no.\n')
            if ee.lower() != 'y':
                break
        except:
            print("You are finish all of rows : \n")
    print('----------------------------------')

    # Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print(counts_of_user_types)
    print('----------------------------------')

    #Counts of gender
    if 'Gender' in df:
        print("\n *** Counts of gender : \n")

       #write gender from df by 5 rows
        x=0
        y=5
        ff =input('\nPlease input y if you want to see 5 row from gender\n And press any key to check gender column in df or not : ').lower()
        while ff=='y':
            try:
                for i in range(1):
                     gender_counts = df['Gender'].iloc[x:y,]
                     print("The 5 row from Gender : \n", gender_counts)
                     x+=5
                     y+=5
                print('----------------------------------')
                ff = input('\nWould you like to proceed? Enter y or no.\n')
                if ff.lower() != 'y':
                    break
            except:
                print("You are finish all of rows : \n")
        print('----------------------------------')

    #Check gender column in df or not
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
    else:
        print('\nSorry file of city you are selected has no gender information\n')

    #Check gender column in df or not
    if 'Birth Year' in df:
        # Display birth year by 5 rows
        x=0
        y=5
        ff =input('\nPlease input y if you want to see min 5 row of Birth Year\n And press any key to display most earliest birth year: ').lower()
        while ff=='y':
            try:
                for i in range(1):
                     birth_year = df['Birth Year'].iloc[x:y,]
                     print("The 5 row from Gender : \n", birth_year)
                     x+=5
                     y+=5
                print('----------------------------------')
                ff = input('\nWould you like to proceed? Enter y or no.\n')
                if ff.lower() != 'y':
                    break
            except:
                print("You are finish all of rows : \n")
        print('----------------------------------')

        # The most earliest birth year
        earliest_year = df['Birth Year'].min()
        print("\nThe earliest birth year: ", earliest_year)

        # The most recent birth year
        most_recent = df['Birth Year'].max()
        print("\nThe most recent birth year: ", most_recent)
        # The most common birth year
        most_common_year = df['Birth Year'].mode()
        print("\nThe most common birth year: ", most_common_year)
    else:
        print('Sorry file of city you are selected has no birthdate information\n')

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
