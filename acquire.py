import pandas as pd
from env import get_db_url
import matplotlib as plt
import seaborn as sns
import numpy as np


def get_zillow_one():
    '''First interation to read the zillow sql database into a pandas dataframe 
        where only the 2017 Single Family residential properties show along with the following columns:
        bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, 
        taxvaluedollarcnt.

        Rename columns to: Bedroom_count, Bathroom_count, square_feet, Assessed_value
    '''

    #Acquire zillow database from MySQL
    sql = """
    SELECT
    bedroomcnt, bathroomcnt,  
    calculatedfinishedsquarefeet,  
    taxvaluedollarcnt, transactiondate,fips
    FROM properties_2017
    JOIN predictions_2017 AS pe USING (parcelid)
    JOIN propertylandusetype USING (propertylandusetypeid)
    WHERE propertylandusetype.propertylandusedesc = 'Single Family Residential'
    AND pe.transactiondate LIKE '2017%';
    """
    return pd.read_sql(sql, get_db_url("zillow"))

#____________________________________________________
    #Dropped all nulls
def handle_nulls(df):    
# We keep 99.41% of the data after dropping nulls
# round(df.dropna().shape[0] / df.shape[0], 4) returned .9941
    df = df.dropna()
    return df

    #Changing dtype of house squarefeet
    #df['calculatedfinishedsquarefeet'] = df['calculatedfinishedsquarefeet'].astype('int')
    
    #Renamed columns for easier reading
    #df = df.rename(columns={"bedroomcnt": "Bedroom_Count", "bathroomcnt": "Bathroom_count", "calculatedfinishedsquarefeet": "square_feet", "taxvaluedollarcnt": "Assessed_Value"})

    #return df