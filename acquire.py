import pandas as pd
import env



def get_zillow_one(df):
    '''First interation to read the zillow sql database into a pandas dataframe 
        where only the 2017 Single Family residential properties show along with the following columns:
        bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, 
        taxvaluedollarcnt.

        Rename columns to: Bedroom_count, Bathroom_count, square_feet, Tax_value
    '''

    #Acquire zillow database from MySQL
    df = pd.read_sql("SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, transactiondate FROM properties_2017 JOIN predictions_2017 USING (id) JOIN propertylandusetype USING (propertylandusetypeid) WHERE propertylandusetype.propertylandusedesc = 'Single Family Residential'; ", env.get_db_url('zillow'))

    #Dropped all nulls
    df = df.dropna()

    #Changing dtype of house squarefeet
    df['calculatedfinishedsquarefeet'] = df['calculatedfinishedsquarefeet'].astype('int')
    
    #Renamed columns for easier reading
    df = df.rename(columns={"bedroomcnt": "Bedroom_Count", "bathroomcnt": "Bathroom_count", "calculatedfinishedsquarefeet": "square_feet", "taxvaluedollarcnt": "Assessed_Value"})

    return df