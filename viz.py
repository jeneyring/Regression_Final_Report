import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


"""
This file is for functions that hold the visualizations for the Zillow 
Regression Model Final Project
"""
def hist_all(train):
    df = wrangle_zillow()
    train, validate, test = split_data(df)
#scaled data
    scale_data(train, validate, test)
#Creating histograms for all the variables (afer split and scaled)

    plt.figure(figsize=(16, 3))

# Creates a List of columns:
    for i, col in enumerate(train.columns):

    # i starts at 0, but plot numbers should start at 1
        plot_number = i + 1 

    # Create subplot.
        plt.subplot(1,8, plot_number)

    # Title with column name.
        plt.title(col)

    # Display histogram for column.
        train[col].hist(bins=5)

    # Hide gridlines.
        plt.grid(False)

def plot_categorical_and_continuous_vars():
    columns = ['bathroomcnt','bedroomcnt']
    for x in columns:
        sns.set()
        fig, axes = plt.subplots(2,2)
        sns.boxplot(x= x, y="taxvaluedollarcnt", data=train, hue = 'county', ax = axes[0,0])
        sns.barplot(x= x, y="taxvaluedollarcnt", data=train, hue = 'county', ax = axes[0,1])
        sns.violinplot(x= x, y="taxvaluedollarcnt", data=train, hue = 'county', ax = axes[1,0])
        sns.scatterplot(x= x, y="taxvaluedollarcnt", data=train, hue = 'county', ax = axes[1,1])
plot_categorical_and_continuous_vars()
    