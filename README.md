# Predicting-Gym-Class-Attendance
Predicting gym class attendance with a dataset on class attendance for GoalZone, 
a fitness club chain in Canada, published on Kaggle. 

## Problem definition
GoalZone has fully booked classes that often have a low attendance rate.
To increase the space available for members who are present in the gym, 
the company would like to anticipate available spaces
by predicting whether a member with a booking will attend class.

## The Dataset
There are 1,500 observations with the following features:
- `booking_id`
- `months_as_member`
- `weight`
- `days_before`
- `day_of_week`
- `time`
- `category`
- `attended` (target)

## Requirements
To use this dataset effectively, you will need:

- Python: Recommended for data processing and analysis.
- Libraries: pandas, numpy, and matplotlib for data manipulation and visualization, and scikit-learn for building predictive models.

data = pd.read_csv("fitness_class_2212.csv")
