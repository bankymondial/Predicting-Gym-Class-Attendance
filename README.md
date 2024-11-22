## Predicting Gym Class Attendance

This project aims to predict gym class attendance using a dataset published on Kaggle by GoalZone, a fitness club chain in Canada. The predictions help identify available spaces in fully booked classes by anticipating whether a member with a booking will attend.

### Problem Definition
GoalZone faces challenges with low attendance rates in fully booked fitness classes. I developed a machine learning model to predict attendance to address this, enabling better space utilization.

### Dataset
The dataset contains 1,500 observations with the following features:
- `booking_id`: Nominal. Unique identifier of the booking.
- `months_as_member`: (Discrete) Number of months as a fitness club member (minimum 1 month).
- `weight`:  (Continuous) Member's weight in kg, rounded to 2 decimal places.
- `days_before`: (Discrete) Number of days before the class the member registered.
- `day_of_week`: (Nominal) Day of the week of the class.
- `time`: (Ordinal) Time of day of the class (`AM` or `PM`).
- `category`: Nominal. (Nominal) Category of the fitness class.
- `attended` (target): (Nominal) Whether the member attended the class (`1` for Yes, `0` for No).
  
____________________________________________________________________________________________________________________________________________________

### Repository Overview
This repository contains:

1. Training Scripts: For building the machine learning model. These are `notebook.ipynb`, `Model training and selection.ipynb` and `train.py`. 
2. Prediction Scripts: For making predictions. These are `predict-test.py`, `predict.py` and `model_C=1.bin`.
3. Deployment Scripts: To deploy the model as a web service using Flask, Waitress, and Docker. These are `Pipfile`, `Pipfile.lock` and `Dockerfile`. 
4. API Documentation: Instructions to use the prediction API locally or via Docker/ECS. This can be found in the README file.
5. This repository also contains the dataset, `fitness_class_2212.csv` which can also be found on [Kaggle](https://www.kaggle.com/datasets/ddosad/datacamps-data-science-associate-certification).
6. Deployment to the cloud: The URL to the deployed service is `http://52.3.242.226:5454/predict`.


____________________________________________________________________________________________________________________________________________________


### Getting Started
Follow these steps to set up, train, and deploy the model on your local machine.

#### Prerequisites
Ensure you have the following installed:
- Python: Version >= 3.12.1
- Pipenv: For dependency management
- Docker: To containerize and deploy the application
- curl: For API testing

____________________________________________________________________________________________________________________________________________________


### Setup and Installation
##### 1. Clone the Repository
    git clone [<repository-url>](https://github.com/bankymondial/Predicting-Gym-Class-Attendance.git)
    cd Predicting-Gym-Class-Attendance
##### 2. Install Dependencies
    pipenv install    
##### 3. Train the Model
   Train the model by running:
   python train.py
_This generates model_C=1.bin, containing the trained model and the DictVectorizer._

____________________________________________________________________________________________________________________________________________________


### Docker for running the service
##### 1. Start the Waitress Server
    Run the Flask app with Waitress:
    waitress-serve --listen=0.0.0.0:5454 predict:app
_The API will start on port 5454._
##### 2. Dockerfile
    Ensure the `Dockerfile` contains the following content:
    FROM python:3.12.1-slim
    RUN pip install pipenv
    WORKDIR /app
    COPY ["Pipfile", "Pipfile.lock", "./"]
    RUN pipenv install --system --deploy
    COPY ["predict.py", "predict-test.py", "model_C=1.bin", "./"]
    EXPOSE 5454
    ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:5454", "predict:app"]
##### 3. Build the Docker Image
    docker build -t predicting-attendance .
##### 4. Run the Docker Container
    docker run -it --rm -p 5454:5454 predicting-attendance
##### 5. Test Predictions
###### - Using curl:
    curl -X POST http://localhost:5454/predict \
    -H "Content-Type: application/json" \
    -d '{"months_as_member": 12, "weight": 70, "category": "Cycling"}'
###### - Using predict-test.py:
    python predict-test.py

____________________________________________________________________________________________________________________________________________________


### Public API URL
##### Base URL: `http://52.3.242.226:5454/`
##### Prediction Endpoint: `http://52.3.242.226:5454/predict`

____________________________________________________________________________________________________________________________________________________


### API Testing with Postman
##### 1. Use the Root Endpoint:
Visit `http://52.3.242.226:5454/` to confirm the API is running.
_Expected Response_:
`"API is running. Use the /predict endpoint for predictions. See README file for instructions."`
##### 2. Use the /predict Endpoint:
    Request Type: POST
    Body (JSON):
        {
            "months_as_member": 12,
            "weight": 70,
            "category": "Cycling"
        }
    Response Example:
        {
            "attended_probability": 0.85,
            "attended": true
        }

____________________________________________________________________________________________________________________________________________________


### Troubleshooting
##### Address Already in Use:
1. Identify the process using port 5454: lsof -i :5454
2. Kill the process using the PID: kill -9 <PID>

##### Restarting the Waitress Server:
waitress-serve --listen=0.0.0.0:5454 predict:app

##### Dependency Issues:
- Verify Python, Pipenv, and Docker versions match the prerequisites.


