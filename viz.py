import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

"""
This file is for functions that hold the visualizations for the Zillow 
Regression Model Final Project
"""
#def hist_all(train):
    #df = wrangle_zillow()
    #train, validate, test = split_data(df)
#scaled data
    #scale_data(train, validate, test)
#Creating histograms for all the variables (afer split and scaled)

    #plt.figure(figsize=(16, 3))

# Creates a List of columns:
    #for i, col in enumerate(train.columns):

    # i starts at 0, but plot numbers should start at 1
        #plot_number = i + 1 

    # Create subplot.
        #plt.subplot(1,8, plot_number)

    # Title with column name.
        #plt.title(col)

    # Display histogram for column.
        #train[col].hist(bins=5)

    # Hide gridlines.
        #plt.grid(False)

#def plot_categorical_and_continuous_vars():
    #columns = ['bathroomcnt','bedroomcnt']
    #for x in columns:
        #sns.set()
        #fig, axes = plt.subplots(2,2)
        #sns.boxplot(x= x, y="taxvaluedollarcnt", data=train, hue = 'county', ax = axes[0,0])
        #sns.barplot(x= x, y="taxvaluedollarcnt", data=train, hue = 'county', ax = axes[0,1])
        #sns.violinplot(x= x, y="taxvaluedollarcnt", data=train, hue = 'county', ax = axes[1,0])
        #sns.scatterplot(x= x, y="taxvaluedollarcnt", data=train, hue = 'county', ax = axes[1,1])
#plot_categorical_and_continuous_vars()
    
#sample = train_scaled.sample(50)
#baseline = sample.baseline
#yhat = sample.yhat
#x = sample.calculatedfinishedsquarefeet
#y = sample.taxvaluedollarcnt




def baseline_v_ols(train_scaled):

    x = train_scaled.calculatedfinishedsquarefeet
    y = train_scaled.taxvaluedollarcnt

    plt.figure(figsize=(8, 5))
## plot data points, regression line and baseline
    # plot the data points 
    plt.scatter(x, y, color='dimgray', s=40)

#### plot the regression line
#obtain m (slope) and b(intercept) of linear regression line
    m, b = np.polyfit(x, y, 1)
#add linear regression line to scatterplot 
    plt.plot(x, m*x+b)

# add baseline through annotation
# for each x apply y to make line across chart
    plt.axhline(train_scaled.taxvaluedollarcnt.mean(), ls = ':')
#### set and plot title, subtitle, and axis labels
# set titles
    title_string = r'Difference in Error'
    subtitle_string = "Baseline vs. Regression Line"

    # add titles
    plt.title(subtitle_string, fontsize=12, color='black')
    plt.suptitle(title_string, y=1, fontsize=14, color='black')
    
    # add axes labels
    plt.ylabel('Property value')
    plt.xlabel('Finished Squarefeet')

# annotate some of the error lines with pointers
    # add pointer: the first data point to the regression line
    plt.annotate('.', xy=(70.25, 70), xytext=(73, 70), xycoords='data', textcoords='data', arrowprops={'arrowstyle': 'fancy', 'color':'darkseagreen', 'linewidth': 1})

    # add pointer: the last data point to the regression line
    plt.annotate('', xy=(100.25, 97), xytext=(103, 97), xycoords='data', textcoords='data', arrowprops={'arrowstyle': 'fancy', 'color':'darkseagreen', 'linewidth': 1})

    # add pointer: the last data point to the baseline 
    plt.annotate('', xy=(100.25, 90), xytext=(103, 90), xycoords='data', textcoords='data', arrowprops={'arrowstyle': 'fancy', 'color':'goldenrod', 'linewidth': 1})

    ## ----------------------------------------
    ## add text to the annotatations
    # the error of the first data point to the regression line
#plt.text(73, 70, 4.1, ha='left', va='center', color='black')

    # the error of the last data point to the regression line
#plt.text(103, 96, 1.6, ha='left', va='center', color='black')

    # the error of the last data point to the baseline
#plt.text(103, 90, -12.7, ha='left', va='center', color='black')
