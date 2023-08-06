# -*- coding: utf-8 -*-

"""
    __  ___      __    _ __     ____  _   _____
   /  |/  /___  / /_  (_) /__  / __ \/ | / /   |
  / /|_/ / __ \/ __ \/ / / _ \/ / / /  |/ / /| |
 / /  / / /_/ / /_/ / / /  __/ /_/ / /|  / ___ |
/_/  /_/\____/_.___/_/_/\___/_____/_/ |_/_/  |_|

HELPER FUNCTIONS

-- Coded by Wouter Durnez
-- mailto:Wouter.Durnez@UGent.be
"""

import os
import random as rnd
import sys
import time
from datetime import datetime
from pprint import PrettyPrinter
from typing import Callable

import numpy as np
import pandas as pd

pp = PrettyPrinter(indent=4)

####################
# GLOBAL VARIABLES #
####################

# Set log level (1 = only top level log messages -> 3 = all log messages)
LOG_LEVEL = 3
DATA_DIR = os.path.join(os.pardir, os.pardir, 'data')
INDICES = {'notifications', 'appevents', 'sessions', 'logs'}
INDEX_FIELDS = {
    'notifications': [
        'application',
        'data_version',
        'id',
        'notificationID',
        'ongoing',
        'posted',
        'priority',
        'studyKey',
        'surveyId',
        'time'],
    'appevents': [
        'application',
        'battery',
        'data_version',
        'startTime',
        'endTime',
        'id',
        'latitude',
        'longitude',
        'model',
        'notification',
        'notificationId',
        'session',
        'studyKey',
        'surveyId'
    ],
    'sessions': [
        'startTime',
        'endTime',
        'data_version',
        'id',
        'sessionID',
        'studyKey',
        'surveyId'
    ],
    'logs': [
        'data_version',
        'id',
        'studyKey',
        'surveyId',
        'logging enabled',
        'date'
    ]
}


####################
# Helper functions #
####################

def set_param(log_level=None, data_dir=None):
    """
    Set mobileDNA parameters.

    :param log_level: new value for log level
    :param data_dir: new data directory
    """

    # Declare these variables to be global
    global LOG_LEVEL
    global DATA_DIR

    # Set log level
    if log_level:
        LOG_LEVEL = log_level

    # Set new data directory
    if data_dir:
        DATA_DIR = data_dir


def log(*message, lvl=3, sep="", title=False):
    """
    Print wrapper that adds timestamp, and can be used to toggle levels of logging info.

    :param message: message to print
    :param lvl: importance of message: level 1 = top importance, level 3 = lowest importance
    :param sep: separator
    :param title: toggle whether this is a title or not
    :return: /
    """

    # Set timezone
    if 'TZ' not in os.environ and sys.platform == 'darwin':
        os.environ['TZ'] = 'Europe/Amsterdam'
        time.tzset()

    # Title always get shown
    lvl = 1 if title else lvl

    # Print if log level is sufficient
    if lvl <= LOG_LEVEL:

        # Print title
        if title:
            n = len(*message)
            print('\n' + (n + 4) * '#')
            print('# ', *message, ' #', sep='')
            print((n + 4) * '#' + '\n')

        # Print regular
        else:
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(str(t), (" - " if sep == "" else "-"), *message, sep=sep)

    return


def time_it(f: Callable):
    """
    Timer decorator: shows how long execution of function took.
    :param f: function to measure
    :return: /
    """

    def timed(*args, **kwargs):
        t1 = time.time()
        res = f(*args, **kwargs)
        t2 = time.time()

        log("\'", f.__name__, "\' took ", round(t2 - t1, 3), " seconds to complete.", sep="")

        return res

    return timed


def set_dir(*dirs):
    """
    If folders don't exist, make them.

    :param dirs: directories to check/create
    :return: None
    """

    for dir in dirs:
        if not os.path.exists(dir):
            os.makedirs(dir)
            log("WARNING: Data directory <{dir}> did not exist yet, and was created.".format(dir=dir), lvl=1)
        else:
            log("\'{}\' folder accounted for.".format(dir), lvl=3)


##################
# Time functions #
##################

def to_timestamp(df: pd.DataFrame, columns: list):
    """MARKED FOR DELETION"""
    for column in columns:
        df[column] = df[column].astype(int) / 10 ** 9


def split_time_range(time_range: tuple, duration: pd.Timedelta, ignore_error=False) -> tuple:
    """
    Takes a time range (formatted strings: '%Y-%m-%dT%H:%M:%S.%f'), and selects
    a random interval within these boundaries of the specified active_screen_time.

    :param time_range: tuple with formatted time strings
    :param duration: timedelta specifying the active_screen_time of the new interval
    :param ignore_error: (bool) if true, the function ignores durations
                         that exceed the original length of the time range
    :return: new time range
    """

    # Convert the time range strings to unix epoch format
    start = datetime.strptime(time_range[0], '%Y-%m-%dT%H:%M:%S.%f').timestamp()
    stop = datetime.strptime(time_range[1], '%Y-%m-%dT%H:%M:%S.%f').timestamp()

    # Calculate total active_screen_time (in seconds) of original
    difference = stop - start

    # Calculate active_screen_time of new interval (in seconds)
    duration = duration.total_seconds()

    # Error handling
    if difference < duration:

        if ignore_error:
            log(
                "WARNING: New interval length exceeds original time range active_screen_time! Returning original time range.")
            return time_range

        else:
            raise Exception('ERROR: New interval length exceeds original time range active_screen_time!')

    # Pick random new start and stop
    new_start = rnd.randint(int(start), int(stop - duration))
    new_stop = new_start + duration

    # Format new time range
    new_time_range = (datetime.fromtimestamp(new_start).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3],
                      datetime.fromtimestamp(new_stop).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3])

    return new_time_range


############################
# Initialization functions #
############################

def hi():
    """
    Say hello. (It's stupid, I know.)
    If there's anything to initialize, do so here.
    """

    print("\n")
    print("    __  ___      __    _ __     ____  _   _____ ")
    print("   /  |/  /___  / /_  (_) /__  / __ \/ | / /   |")
    print("  / /|_/ / __ \/ __ \/ / / _ \/ / / /  |/ / /| |")
    print(" / /  / / /_/ / /_/ / / /  __/ /_/ / /|  / ___ |")
    print("/_/  /_/\____/_.___/_/_/\___/_____/_/ |_/_/  |_|")
    print("\n")

    print("LOG_LEVEL is set to {}.".format(LOG_LEVEL))
    print("DATA_DIR is set to {}".format(DATA_DIR))
    print()

    # Set this warning if you intend to keep working on the same data frame,
    # and you're not too worried about messing up the raw data.
    pd.set_option('chained_assignment', None)
    rnd.seed(616)

########################
# Data frame functions #
########################

def check_index(df: pd.DataFrame, index: str, ignore_error=False) -> bool:
    """
    Checks if a data frame is indeed of the right index type.

    :param df: data frame that will be checked
    :param index: type of data that is expected
    :return: (bool) checks out (True) or doesn't (False)
    """

    # Check index argument
    if index not in INDICES:
        raise Exception(
            "ERROR: When checking index type, please enter valid index ('appevents','notifications','logs', or 'sessions'.")

    unique_columns = {
        'appevents': 'session',
        'notifications': 'time',
        'sessions': 'session on',
        'logs': 'date'
    }

    # Check what type of data we're dealing with in reality
    true_index = None

    # Go over unique columns, and check if they're in our data frame
    for unique_key in unique_columns.keys():

        # If they are, that's the type of data frame we're dealing with
        if unique_columns[unique_key] in df:
            true_index = unique_key
            break

    # If our data type is not what we expected, return False (or throw an error)
    if true_index != index:
        if ignore_error:
            log(f"Unexpected index! Expected <{index}>, but got <{true_index}>.", lvl=3)
            return False
        else:
            raise Exception(f"ERROR: Unexpected index! Expected <{index}>, but got <{true_index}>.")

    # ...else return that check is A-OK
    return True


def format_data(df: pd.DataFrame, index: str) -> pd.DataFrame:
    """
    Set the data types of each column in a data frame, depending on the index.
    This is done to save memory.

    :param df: data frame to format
    :param index: type of data
    :return: formatted data frame
    """

    # Check if index is valid
    if index not in INDICES:
        raise Exception("ERROR: Invalid doc type! Please choose 'appevents', 'notifications', 'sessions', or 'logs'.")

    elif index == 'appevents':

        # Reformat data version (trying to convert to int)
        df.data_version = pd.to_numeric(df.data_version, downcast='float')

        # Format timestamps
        df.startTime = pd.to_datetime(df.startTime).astype(int)
        df.endTime = pd.to_datetime(df.endTime).astype(int)

        # Downcast lat/long
        df.latitude = pd.to_numeric(df.latitude, downcast='float')
        df.longitude = pd.to_numeric(df.longitude, downcast='float')

        # Downcast battery column
        df.battery = df.battery.astype('uint8')

        # Factorize categorical variables (ids, apps, session numbers, etc.)
        to_category = ['id','application','session','studyKey','surveyId','model']
        for column in to_category:
            df[column] = df[column].astype('category')


    elif index == 'notifications':

        df.time = pd.to_datetime(df['time'])
        df.id = df.id.astype('category')
        df.application = df.application.astype('category')
        df.notificationID = df.notificationID.astype('category')
        df.studyKey = df.studyKey.astype('category')
        df.surveyId = df.surveyId.astype('category')

    elif index == 'sessions':

        # Convert to timestamp
        df['timestamp'] = pd.to_datetime(df['timestamp']).astype(int)

        # Sort data frame
        df.sort_values(by=['id', 'timestamp'], inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.rename(columns={'timestamp': 'startTime'}, inplace=True)

        # Add end timestamp
        df['endTime'] = df.groupby('id')['startTime'].shift(-1)
        df['session off'] = df.groupby('id')['session on'].shift(-1)

        # Add ID which links with appevents index
        df['sessionID'] = pd.to_numeric(df['startTime'].astype(int) - 3600, downcast='unsigned')

        # Filter out bogus rows
        df = df.loc[(df['session on'] == True) & (df['session off'] == False)]

    elif index == 'logs':

        df['date'] = pd.to_datetime(df['date'])

    for col in df.columns:

        if col.startswith('Unnamed') or col not in INDEX_FIELDS[index]:
            df.drop(labels=[col], axis=1, inplace=True)

    log("Successfully formatted dataframe.", lvl=3)

    return df


def add_duration(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate app event duration and add to (new) data frame.

    :param df: data frame to process (should be appevents index)
    :return: modified data frame
    """

    # Check if data contains necessary columns
    if 'startTime' not in df.columns or \
            'endTime' not in df.columns:
        raise Exception("ERROR: Necessary columns missing!")

    # Calculate duration (in seconds)
    try:
        df['duration'] = df['endTime'] - df['startTime']
    except:
        raise Exception("ERROR: Failed to calculate duration!")

    # Check if there are any negative durations.
    if not df[df["duration"] < 0].empty:
        log("WARNING: encountered negative duration!", lvl=1)

    return df


def get_unique(column: str, df: pd.DataFrame) -> np.ndarray:
    """
    Get list of unique column values in given data frame.

    :param column: column to sift through
    :param df: data frame to look in
    :return: unique values in given column
    """

    try:
        unique_values = df[column].unique()
    except:
        raise Exception("ERROR: Could not find variable {column} in dataframe.".format(column=column))

    return unique_values


#####################
# Storage functions #
#####################

def save(df: pd.DataFrame, dir: str, name: str, csv_file=True, pickle=False, parquet=False):
    """
    Wrapper function to save mobileDNA data frames.

    :param df: data to store on disk
    :param dir: location to store it in
    :param name: name of the file
    :param csv_file: save in CSV format (bool)
    :param pickle: save in pickle format (bool)
    :param parquet: save in parquet format (bool)
    :return: /
    """

    path = os.path.join(dir, name)

    # Store to CSV
    if csv_file:

        # Try and save it
        try:

            df.to_csv(path_or_buf=path + ".csv", sep=";", decimal='.')
            log("Saved data frame to {}".format(path + ".csv_file"))

        except Exception as e:

            log("ERROR: Failed to store data frame as CSV! {e}".format(e=e), lvl=1)

    # Store to pickle
    if pickle:

        try:

            df.to_pickle(path=path + ".pkl")
            log("Saved data frame to {}".format(path + ".pkl"))

        except Exception as e:

            log("ERROR: Failed to pickle data frame! {e}".format(e=e), lvl=1)

    # Store to parquet
    if parquet:

        try:
            df.to_parquet(fname=path + ".parquet", engine='auto', compression='snappy')
            log("Saved data frame to {}".format(path + ".parquet"))

        except Exception as e:

            log("ERROR: Failed to store data frame as parquet! {e}".format(e=e), lvl=1)

@time_it
def load(path: str, index: str, file_type='infer', sep=';', dec='.') -> pd.DataFrame:
    """
    Wrapper function to load mobileDNA data frames.

    :param path: location of data frame
    :param index: type of mobileDNA data
    :param file_type: file type (default: infer from path, other options: pickle, csv, or parquet)
    :param sep: field separator
    :param dec: decimal symbol
    :param format: format data frame to save space (watch out for redundant formatting!)
    :return: data frame
    """

    # Check if index is valid
    if index not in INDICES:
        raise Exception("Invalid doc type! Please choose 'appevents', 'notifications', 'sessions', or 'logs'.")

    # Load data frame, depending on file type
    if file_type == 'infer':

        # Get extension
        file_type = path.split('.')[-1]

        # Only allow the following extensions
        if file_type not in ['csv', 'pickle', 'pkl', 'parquet']:
            raise Exception("ERROR: Could not infer file type!")

        log("Recognized file type as <{type}>.".format(type=file_type), lvl=3)

    # CSV
    if file_type == 'csv':
        df = pd.read_csv(filepath_or_buffer=path,
                         # usecols=,
                         sep=sep, decimal=dec,
                         error_bad_lines=False)

    # Pickle
    elif file_type == 'pickle' or file_type == 'pkl':
        df = pd.read_pickle(path=path)

    # Parquet
    elif file_type == 'parquet':
        df = pd.read_parquet(path=path, engine='auto')

    # Unknown
    else:
        raise Exception("ERROR: You want me to read what now? Invalid file type! ")

    # If there's nothing there, just go ahead and return the empty df
    if df.empty:
        return df

    # Drop 'Unnamed' columns
    for col in df.columns:

        if col.startswith('Unnamed'):
            df.drop(labels=[col], axis=1, inplace=True)

    # Add duration if necessary
    if 'duration' not in df and (
            check_index(df=df, index='appevents', ignore_error=True) or
            check_index(df=df, index='sessions', ignore_error=True)):
        add_duration(df)

    return df


########
# MAIN #
########

if __name__ in ['__main__', 'builtins']:
    # Howdy
    hi()

    ts = '2019-11-04 21:43:16.139000'
    # start = pd.to_numeric(pd.to_datetime(df.startTime).astype(int) / 10 ** 9, downcast='unsigned')

    # logs = load(path=os.path.join(DATA_DIR,"log_test_logs.parquet"), index='logs')

    # df = pd.read_parquet(path=os.path.join(DATA_DIR, "glance_small_appevents.parquet"), engine='auto')

    # df2 = load(path=os.path.join(DATA_DIR, "glance_small_appevents.parquet"), index='appevents')
