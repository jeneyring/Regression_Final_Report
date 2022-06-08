"""
Functions that are being used for the Final Report jupyter notebook in relation to
the Zillow project.

Below each function lists its use (and how to use!)
"""
import pandas as pd
import numpy as np
import prepare
import env
import acquire
#for modeling and evaluation
from scipy import stats
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression 
from math import sqrt
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


def get_a_baseline(y_train, y_validate):
# We need y_train and y_validate to be dataframes to append the new columns with predicted values. 
    y_train_baseline = pd.DataFrame(y_train)
    y_validate_baseline = pd.DataFrame(y_validate)

    # 1. Predict Property Value mean
    value_pred_mean = y_train_baseline['taxvaluedollarcnt'].mean()
    y_train_baseline['value_pred_mean'] = value_pred_mean
    y_validate_baseline['value_pred_mean'] = value_pred_mean

    # 2. compute Property value mean
    value_pred_median = y_train_baseline['taxvaluedollarcnt'].median()
    y_train_baseline['value_pred_median'] = value_pred_median
    y_validate_baseline['value_pred_median'] = value_pred_median

    # 3. RMSE of Property value mean
    rmse_train_baseline = mean_squared_error(y_train_baseline.taxvaluedollarcnt, y_train_baseline.value_pred_mean)**(1/2)
    rmse_validate_baseline = mean_squared_error(y_validate_baseline.taxvaluedollarcnt, y_validate_baseline.value_pred_mean)**(1/2)

    print("RMSE_baseline using Mean\nTrain/In-Sample: ", round(rmse_train_baseline, 2), 
        "\nValidate/Out-of-Sample: ", round(rmse_validate_baseline, 2))

    # 4. RMSE of Property Value me
    rmse_train_baseline = mean_squared_error(y_train_baseline.taxvaluedollarcnt, y_train_baseline.value_pred_median)**(1/2)
    rmse_validate_baseline = mean_squared_error(y_validate_baseline.taxvaluedollarcnt, y_validate_baseline.value_pred_median)**(1/2)

    print("RMSE_baseline using Median\nTrain/In-Sample: ", round(rmse_train_baseline, 2), 
        "\nValidate/Out-of-Sample: ", round(rmse_validate_baseline, 2))

def baseline_df(y_train):
    #creates the baseline dataframe with yhat, mean values, 
    #creating the zillow predictor baseline aka mean, of taxvaluedollarcnt(y)
    baseline = y_train.taxvaluedollarcnt.mean()
    #let's add the baseline to the the dataframe
    y_train['baseline'] = y_train.taxvaluedollarcnt.mean()
    #let's add the yhat_baseline to df too
    y_train['yhat'] = predictions

    #to call: baseline_df(y_train), then in notebook: y_train.head()

#_____________________________________________


def ols_model(y_train, y_validate):
    """
    A simple function to write out the OLS (linear regression) model used in the 
    notebook. 
    """
# create the model object
    lm = LinearRegression(normalize=True)

# fit the model to our training data. We must specify the column in y_train, 
# since we have converted it to a dataframe from a series! 
    lm.fit(X_train, y_train.taxvaluedollarcnt)

# predict train
    y_train['value_pred_lm'] = lm.predict(X_train)

# evaluate: rmse
    rmse_train = mean_squared_error(y_train.taxvaluedollarcnt, y_train.value_pred_lm)**(1/2)

# predict validate
    y_validate['value_pred_lm'] = lm.predict(X_validate)

# evaluate: rmse
    rmse_validate = mean_squared_error(y_validate.taxvaluedollarcnt, y_validate.value_pred_lm)**(1/2)

    print("RMSE for OLS using LinearRegression\nTraining/In-Sample: ", rmse_train, 
      "\nValidation/Out-of-Sample: ", rmse_validate)

    print('Difference of Train vs Validate model:', rmse_validate-rmse_train)

#_____________________________________________

def add_residuals(y_train):
    """
    adding residual columns for OLS model
    """
    y_train['residual'] = y_train.taxvaluedollarcnt - y_train.yhat
    y_train['baseline_residual'] = y_train.taxvaluedollarcnt - y_train.baseline 

#_____________________________________________

