# Zillow 2017 Single Family Properties 
# Property Tax Predictions Model

## <u> Project Description: </u>
>This is my final project to assess the lead drivers for property value at Zillow. 

><b>In this project I will explore and Hypothesis test the Zillow dataset to find any linear relations between different property features and property value.

>I then will construct a ML Regression model that can beat accuracy predictions over Zillow's current property value predictors.</b>


AUDIENCE NOTE: Included in the Final Report file, there is Scratchpad file with the step-by-step process of the key findings of how the key driver(s) were found, the models and their accuracy used in creating the ML model, variance score results and what the outcomes vs. my initial hypothesis were.

The Final_Report file is a small snippet of the Scratchpad walkthrough, to show and present a 5 min Live presentation to the data science team. 

### <b>Project Goals:</b><br>
>- To find the property feature drivers of Zillow's property value predictions.
>- To create a Regression ML model that can beat the accuracy prediction rate of Zillow's current model (aka baseline model).
## <u> Original Hypothesis: </u>

## <u> Data Dictionary: </u>
|Target|Datatype|Definition|
|:-------|:--------|:----------|
| zillow | 52441 non-null: float64 | Zillow's 2017 predictions & transactions dataset |

|Feature|Datatype|Definition|
|:-------|:--------|:----------|
| bedroomcnt          |  52441 non-null: float64 | bedroom count of 2017 data |
| bathroomcnt         |  52441 non-null: float64  | bathroom count of 2017 data|
| calculatedfinishedsqft   | 52441 non-null: float64 | finished property sqft|
| taxvaluedollarcnt       |  52441 non-null: float64 | Property Value |
| transactiondate   |  52441 non-null: object | date of property transactions|
| fips |  52441 non-null: float64 | non-null: float64| fips code (county/state)|

## <u> How to Replicate: </u>
- download project files
- call in dataset using 'from wrangle import wrangle_data()' {attached in wrangle.py}
- call in prepare, scale and split data from the functions in prepare.py file
- explore visualizations from the viz.py functions
- create the models from the model.py file

#### Hypothesis 1 
> - alpha = 0.05
> - H0: There is NO linear dependancy between bathroom count and property value
> - Ha: There is a linear dependancy between bathroom count and property value
> - <b>Outcome: I rejected the Null Hypothesis, in that there is a linear dependancy with bathroom count and property value.</b>

#### Hypothesis 2 
> - alpha = 0.05
> - H0: There is NO linear dependancy between bedroom count and property value
> - Ha: There is a linear dependancy between bedroom count and property value
> - <b>Outcome: I rejected the Null Hypothesis, in that there is a linear dependancy with bathroom count and property value.</b>

<hr style="border-top: 10px green; margin-top: 1px; margin-bottom: 1px"></hr>


 ### <b>Project Planning (aka How I think I'll get there!):</b><br>
 <b>STEPS AHEAD:</b><br>
 - Explore these 5 property features variables and determine if drivers for property value:
    1) bedroom count
    2) bathroom count
    3) finished square feet
    4) country
    5) transaction date (time of year sold)
  Using exploration techniques (ie. charts, crosstabs, hypothesis testing)
 - Create regression models to train, validate, and test drivers on.



 <b>MY PROJECT CHECK-LIST:</b><br>
 - Create acquire and prepare.py/wrangle.py modules
 - Log down process and questions/takeaways along the way
 - Construct ML models


 - <b> FINAL REPORT: </b><br>
    - use markdown to guide audience
      - (all cells with code need comments!)
    - Begin project with Overview and Goals
    - End project with a Conclusion (how relates to beginning goals)
    - Exploration portion only has charts/data that is important
    - Include 4 visualizations: Question | Visualization | Statistical Test (at least 2 | 
             - <i> must</i> provide markdown for these visuals
    - Provide context of target variable to visualization parameters
    - Include 3 best models 
         - Show steps and code to fit/evaluate/ and select those models
    -On best model, chart visually how it performed on its test