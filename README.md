# Predicting Gym Class Attendance
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

## This repository contains a machine learning project for predicting gym class attendance using a trained model. The project includes scripts to train the model, make predictions, and deploy the model as a web service using Flask, Waitress, and Docker.

## Getting Started
Follow these instructions to run predictions on your computer.

## Dependencies
Ensure you have the following installed:

Python (>=3.12.1)
Pipenv
Docker
curl (for API testing)

## Setup and Installation
1. Clone the Repository
Clone the repository to your local machine:
git clone <repository-url>
cd Predicting-Gym-Class-Attendance

2. Install Dependencies
Run the following commands to set up a virtual environment and install dependencies:
pipenv shell
pipenv install

3. Train the Model
Train the model by running:
python train.py
_This will generate a file named model_C=1.bin, which contains the trained model and DictVectorizer._

## Running the Prediction Locally
1. Start the Waitress Server
Run the Flask app using Waitress:
waitress-serve --listen=0.0.0.0:5454 predict:app
_This will start the API on port 5454._

2. Make a Prediction
You can make a prediction using either curl or the predict-test.py script:
Using curl:
curl -X POST http://localhost:5454/predict \
-H "Content-Type: application/json" \
-d '{"months_as_member": 12, "weight": 70, "category": "Cycling"}'

Using predict-test.py
Run the script to test predictions:
python predict-test.py

## Using Docker
1. Write the Dockerfile
Ensure the Dockerfile contains the following content:
FROM python:3.12.1-slim
RUN pip install pipenv
WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pipenv install --system --deploy
COPY ["predict.py", "predict-test.py", "model_C=1.bin", "./"]
EXPOSE 5454
ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:5454", "predict:app"]
_Use gunicorn instead of waitress on Linux._

2. Build the Docker Image
Build the Docker image with the following command:
docker build -t predicting-attendance .

3. Run the Docker Container
Run the container:
docker run -it --rm -p 5454:5454 predicting-attendance

## Stopping and Restarting the Port
### Checking for Port Usage
If port 5454 is already in use, identify the process using it:
lsof -i :5454

### Stopping the Process
Kill the process using the identified PID:
kill -9 <PID>

### Restarting the Waitress Server
If you need to restart the server, use:
waitress-serve --listen=0.0.0.0:5454 predict:app

### Making Predictions with Docker
4. After running the Docker container, open a new terminal and run the following to make predictions:
If using curl:
curl -X POST http://localhost:5454/predict \
-H "Content-Type: application/json" \
-d '{"months_as_member": 12, "weight": 70, "category": "Cycling"}'

If using predict-test.py: Run the script locally to test the deployed container:
python predict-test.py

Optional: Explore the Docker Container
If you want to inspect the container, open a Bash terminal inside it:
docker run -it --rm --entrypoint=bash predicting-attendance

## Public API URL
Use the following API endpoint for predictions:
- Base URL: `http://52.3.242.226:5454/`
- Prediction Endpoint: `http://52.3.242.226:5454/predict`

## /predict Endpoint Instructions
You can test the /predict endpoint using Postman or other API testing tools:
- Description: Predicts whether a member will attend the class based on input features.
1. Open Postman and create a new request.
2. Set the request type to POST.
3. In the request body, choose the raw option and set the format to JSON.
4. Add the following JSON payload in the body:

    {
        "months_as_member": 12,
        "weight": 70,
        "category": "Cycling"
    }
5. Send the request to http://52.3.242.226:5454/predict.
6. You will receive a JSON response similar to:

    {
        "attended_probability": 0.85,
        "attended": true
    }

Note: Feel free to edit the features and values in the JSON payload to get different predictions.

## Troubleshooting
Address Already in Use:
Use lsof and kill commands as described above to free up port 5454.
Dependency Issues:

Ensure you’re using the correct Python, Pipenv, and Docker versions.