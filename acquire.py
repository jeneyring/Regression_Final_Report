import pandas as pd
import os
from env import get_db_url
import matplotlib as plt
import seaborn as sns
import numpy as np


"""
This is the acquire file for the Zillow 2017 predictions database. 
These files will be pulling the zillow data from the MySQL database to 
collect the properties_2017, predictions_2017 and propertylandusetype tables.

How to use this py file: 
Use `from wrangle import wrangle_zillow` at the top of your notebook.

"""
def get_zillow_data():
    """Will try to read the collected zillow.csv file first """
    filename = "zillow.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        return get_new_zillow_data()

def get_new_zillow_data():
    """Returns a dataframe of all 2017 transactioned properties that are classed as Single Family Residential"""

    sql = """
    select 
    bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, transactiondate, fips
    from properties_2017
    join propertylandusetype using (propertylandusetypeid)
    join predictions_2017 using (parcelid)
    where propertylandusedesc = "Single Family Residential
    and predictions_2017.transactiondate like '2017%%' "
    """
    return pd.read_sql(sql, get_db_url("zillow"))


def handle_nulls(df):    
    # We still have 99.8% of our dataset left after dropping all nulls
    df = df.dropna()
    return df


def change_dtypes(df):
    # Convert some columns to integers
    # fips, yearbuilt, and bedrooms can be integers
    df["fips"] = df["fips"].astype(int)
    df["bedroomcnt"] = df["bedroomcnt"].astype(int)    
    df["taxvaluedollarcnt"] = df["taxvaluedollarcnt"].astype(int)
    df["calculatedfinishedsquarefeet"] = df["calculatedfinishedsquarefeet"].astype(int)
    return df



def handle_outliers(df):
    """Manually handle outliers that do not represent properties likely for 99.8% of buyers and zillow visitors"""
    df = df[df.calculatedfinishedsquarefeet <= 9_000]
    
    df = df[df.calculatedfinishedsquarefeet >= 200]

    df = df[df.bedroomcnt <= 6]

    df=df[df.bedroomcnt != 0]

    df = df[df.bathroomcnt <= 6]

    df=df[df.bathroomcnt != 0]

    df = df[df.taxvaluedollarcnt <= 2_500_000]

    df = df[df.taxvaluedollarcnt >= 45_000]

    return df

#using a function to set the Fips codes into their different counties.
def clearing_fips(df):
    '''This function takes in a DataFrame of unprepared Zillow information and generates a new
    'county' column, with the county name based on the FIPS code. 
    '''
    # create a list of our conditions
    fips = [
        (df['fips'] == 6037),
        (df['fips'] == 6059),
        (df['fips'] == 6111)
        ]
    # create a list of the values we want to assign for each condition
    counties = ['Los Angeles County', 'Orange County', 'Ventura County']
    # create a new column and use np.select to assign values to it using our lists as arguments
    df['county'] = np.select(fips, counties)
    return df


def wrangle_zillow():
    """
    Acquires Zillow data
    Handles nulls
    optimizes or fixes data types
    handles outliers w/ manual logic
    returns a clean dataframe
    """
    df = get_zillow_data()

    df = handle_nulls(df)

    df = change_dtypes(df)

    df = handle_outliers(df)

    df = clearing_fips(df)

    df.to_csv("zillow.csv", index=False)

    return df
