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
- `booking_id`: Nominal. The unique identifier of the booking.
- `months_as_member`: Discrete. The number of months as this fitness club member, minimum 1 month.
- `weight`: Continuous. The member's weight in kg, rounded to 2 decimal places.
- `days_before`: Discrete. The number of days before the class the member registered.
- `day_of_week`: Nominal. The day of the week of the class.
- `time`: Ordinal. The time of day of the class. Either AM or PM.
- `category`: Nominal. The category of the fitness class.
- `attended` (target): Nominal. Whether the member attended the class (1) or not (0).

## Requirements
To use this dataset effectively, you will need:

- Python: Recommended for data processing and analysis.
- Libraries: pandas, numpy, and matplotlib for data manipulation and visualization, and scikit-learn for building predictive models.

data = pd.read_csv("fitness_class_2212.csv")
