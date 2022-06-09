import numpy as np
import matplotlib as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import pandas as pd

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

#first I will drop the columns not needed (or scaled) to fit 
# the calculatedfinishedsquarefeet onto a Linear regression model
def drop_columns_ols(train, validate, test):
    train_scaled = train.copy()
    validate_scaled = validate.copy()
    test_scaled = test.copy()

    train_scaled.drop(columns = ['bedroomcnt', 'bathroomcnt', 'fips','month'], inplace=True)
    return train_scaled

def X_y_models(train_scaled, validate_scaled, test_scaled):

    X_train = train_scaled[['bedroomcnt', 'bathroomcnt', 'taxvaluedollarcnt', 'calculatedfinishedsquarefeet','fips','transactionid','month']]
    y_train = train_scaled['taxvaluedollarcnt']

    X_validate = validate_scaled[['bedroomcnt', 'bathroomcnt', 'taxvaluedollarcnt', 'calculatedfinishedsquarefeet','fips','transactionid','month']]
    y_validate = validate_scaled['taxvaluedollarcnt']

    X_test = test_scaled[['bedroomcnt', 'bathroomcnt', 'taxvaluedollarcnt', 'calculatedfinishedsquarefeet','fips','transactionid','month']]
    y_test = test_scaled['taxvaluedollarcnt']



#creating a new df for evaluating models specifically:
def X_y_train(train, validate, test):
    train_scaled = train.copy()
    validate_scaled = validate.copy()
    test_scaled = test.copy()

    X_train = train_scaled[['calculatedfinishedsquarefeet']]
    y_train = train_scaled['taxvaluedollarcnt']

    X_validate = validate_scaled[['calculatedfinishedsquarefeet']]
    y_validate = validate_scaled['taxvaluedollarcnt']

    X_test = test_scaled[['calculatedfinishedsquarefeet']]
    y_test = test_scaled['taxvaluedollarcnt']
"""
This is a py file that uses the Zillow data set to plot actual and predicted residuals
to evaluate linear regression models.
"""
def plot_residuals(actual, predicted):
    residuals = actual - predicted
    plt.hlines(0, actual.min(), actual.max(), ls=':')
    plt.scatter(actual, residuals)
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title('Actual vs Residual')
    plt.show()


def residuals(actual, predicted):
    return actual - predicted

def sse(actual, predicted):
    return (residuals(actual, predicted) **2).sum()

def mse(actual, predicted):
    n = actual.shape[0]
    return sse(actual, predicted) / n

def rmse(actual, predicted):
    return math.sqrt(mse(actual, predicted))

def ess(actual, predicted):
    return ((predicted - actual.mean()) ** 2).sum()

def tss(actual):
    return ((actual - actual.mean()) ** 2).sum()

def r2_score(actual, predicted):
    return ess(actual, predicted) / tss(actual)

def regression_errors(actual, predicted):
    return pd.Series({
        'sse': sse(actual, predicted),
        'ess': ess(actual, predicted),
        'tss': tss(actual),
        'mse': mse(actual, predicted),
        'rmse': rmse(actual, predicted),
    })

def baseline_mean_errors(actual):
    predicted = actual.mean()
    return {
        'sse': sse(actual, predicted),
        'mse': mse(actual, predicted),
        'rmse': rmse(actual, predicted),
    }

def better_than_baseline(actual, predicted):
    rmse_baseline = rmse(actual, actual.mean())
    rmse_model = rmse(actual, predicted)
    return rmse_model < rmse_baseline