import pandas as pd
import env
import numpy as np
from wrangle import wrangle_zillow
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split



def split_data(df):
    '''
    take in a DataFrame and return train, validate, and test DataFrames; stratify on species.
    return train, validate, test DataFrames.
    '''
    
    # splits df into train_validate and test using train_test_split() stratifying on species to get an even mix of each species
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.fips)
    
    # splits train_validate into train and validate using train_test_split() stratifying on species to get an even mix of each species
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.fips)
    return train, validate, test
#to use, type 'split_data('add your df here')

#____________________________________________________________

#here is my data pipeline function for scaling the zillow dataset:
def scale_data(train,
              validate,
              test,
              columns_to_scale=['bedroomcnt', 'bathroomcnt', 'taxvaluedollarcnt', 'calculatedfinishedsquarefeet'],
              return_scaler=False):
    """
    Scales the 3 data splits.
    Takes in train, validate and test data splits and then returns their scaled counterparts.
    If return_scaler is True, the scaler object will be returned as well
    """
    train_scaled = train.copy()
    validate_scaled = validate.copy()
    test_scaled = test.copy()
    
    #using MinMaxScaler (best showing distribution once scaled)
    scaler = MinMaxScaler()
    scaler.fit(train[columns_to_scale])
    
    #creating a df that puts MinMaxScaler to work on the wanted columns and returns the split datasets and counterparts
    train_scaled[columns_to_scale] = pd.DataFrame(scaler.transform(train[columns_to_scale]),
                                                 columns=train[columns_to_scale].columns.values).set_index([train.index.values])
    
    validate_scaled[columns_to_scale] = pd.DataFrame(scaler.transform(validate[columns_to_scale]),
                                                 columns=validate[columns_to_scale].columns.values).set_index([validate.index.values])
    
    test_scaled[columns_to_scale] = pd.DataFrame(scaler.transform(test[columns_to_scale]),
                                                 columns=test[columns_to_scale].columns.values).set_index([test.index.values])
    
    if return_scaler:
        return scaler, train_scaled, validate_scaled, test_scaled
    else:
        return train_scaled, validate_scaled, test_scaled

#to use: 
    # type "scaler, train_scaled, validate_scaled, test_scaled = scale_data(train, validate, test, return_scaler=True)"
    #into your notebook. then type 'train_scaled' or 'validate_scaled' or 'test_scaled' to view copy of scaled df

#creating another version of the scaler, as after evaluating, I need another split:
def scale_data2(train,
              validate,
              test,
              columns_to_scale=['bedroomcnt', 'bathroomcnt', 'taxvaluedollarcnt', 'calculatedfinishedsquarefeet'],
              return_scaler=False):
    """
    Scales the 3 data splits.
    Takes in train, validate and test data splits and then returns their scaled counterparts.
    If return_scaler is True, the scaler object will be returned as well
    """
    train_scaled2 = train.copy()
    validate_scaled2 = validate.copy()
    test_scaled2 = test.copy()
    
    #using MinMaxScaler (best showing distribution once scaled)
    scaler = MinMaxScaler()
    scaler.fit(train[columns_to_scale])
    
    #creating a df that puts MinMaxScaler to work on the wanted columns and returns the split datasets and counterparts
    train_scaled2[columns_to_scale] = pd.DataFrame(scaler.transform(train[columns_to_scale]),
                                                 columns=train[columns_to_scale].columns.values).set_index([train.index.values])
    
    validate_scaled2[columns_to_scale] = pd.DataFrame(scaler.transform(validate[columns_to_scale]),
                                                 columns=validate[columns_to_scale].columns.values).set_index([validate.index.values])
    
    test_scaled2[columns_to_scale] = pd.DataFrame(scaler.transform(test[columns_to_scale]),
                                                 columns=test[columns_to_scale].columns.values).set_index([test.index.values])
    
    if return_scaler:
        return scaler, train_scaled2, validate_scaled2, test_scaled2
    else:
        return train_scaled2, validate_scaled2, test_scaled2