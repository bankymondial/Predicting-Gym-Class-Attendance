## Predicting Gym Class Attendance

This project aims to predict gym class attendance using a dataset published on Kaggle by GoalZone, a fitness club chain in Canada. The predictions help identify available spaces in fully booked classes by anticipating whether a member with a booking will attend.

### Problem Definition
GoalZone faces challenges with low attendance rates in fully booked fitness classes. I developed a machine learning model to predict attendance to address this, enabling better space utilization.

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


### Instructions for Running the Project
To predict gym class attendance using the trained model, follow these chronological steps:

#### 1. Prerequisites
Ensure you have the following installed:
- Python: Version >= 3.12.1
- Pipenv: For dependency management
- Docker: To containerize and deploy the application
- curl: For API testing

____________________________________________________________________________________________________________________________________________________


#### 2. Setup and Installation
##### 2.1. Clone the Repository
Clone the project to your local machine and navigate into the directory:
    git clone https://github.com/bankymondial/Predicting-Gym-Class-Attendance.git
    cd Predicting-Gym-Class-Attendance
    
##### 2.2 Install Dependencies
Set up a virtual environment and install the necessary Python packages:
    pipenv install
    
##### 2.3 Train the Model (optional)
To retrain the model, run the training script:
   python train.py
   
_This generates `model_C=1.bin`, which contains the trained model and the DictVectorizer._

____________________________________________________________________________________________________________________________________________________


### 3. Running the Prediction Locally
##### 3.1 Start the Waitress Server
Run the Flask app with Waitress:
    waitress-serve --listen=0.0.0.0:5454 predict:app
_The API will be accessible at `http://localhost:5454/`._

##### 3.2 Make Predictions
    You can test predictions using `curl` or the provided `predict-test.py` script:
###### - Using Curl
    curl -X POST http://localhost:5454/predict \
    -H "Content-Type: application/json" \
    -d '{"months_as_member": 12, "weight": 70, "category": "Cycling"}'
###### - Using the Python script:
    python predict-test.py

### 4. Running the Prediction with Docker
##### 4.1 Build the Docker Image
Build the Docker container for the project:
docker build -t predicting-attendance .

##### 4.2 Run the Docker Container
Run the container to start the service:
docker run -it --rm -p 5454:5454 predicting-attendance

##### 4.3 Test Predictions
Test predictions using the same `curl` command or `predict-test.py` as described above. Ensure the service is running on `http://localhost:5454/`.

____________________________________________________________________________________________________________________________________________________


### 5. Accessing the Deployed Model via API
The model is deployed on AWS ECS and can be accessed via the public API. To test predictions:
##### 5.1 Confirm the API is Running
Visit the root endpoint to verify:
    http://52.3.242.226:5454/
Expected response:
    API is running. Use the /predict endpoint for predictions. See README file for instructions.

##### 5.2 Use the Prediction Endpoint
To make predictions, send a `POST` request to the following URL:
    http://52.3.242.226:5454/predict
    - Request Body (JSON):
        {
            "months_as_member": 12,
            "weight": 70,
            "category": "Cycling"
        }

    - Example Response:
        {
            "attended_probability": 0.85,
            "attended": true
        }

##### A Tool for Making POST Requests
###### - Postman: A user-friendly interface for sending POST requests and viewing responses.
          - Instructions:
              1. Create a new request in Postman.
              2. Set the request type to `POST`.
              3. Enter the prediction endpoint URL: `http://52.3.242.226:5454/predict`.
              4. In the request body, select `raw` and set the format to JSON.
              5. Copy and paste the JSON payload (example provided above) into the body.
              6. Send the request and view the response.
Feel free to modify the values of the features (e.g., months_as_member, weight, or category) in the JSON payload to test different scenarios and predictions.

____________________________________________________________________________________________________________________________________________________


### 6. Common Issues and Resolutions.
##### Address Already in Use:
If port 5454 is already in use:
1. Identify the process using port 5454: lsof -i :5454
2. Kill the process using the PID: kill -9 <PID>

##### Restart the Waitress Server:
If the server stops, restart it using:
waitress-serve --listen=0.0.0.0:5454 predict:app

##### Dependency Issues:
- Verify Python, Pipenv, and Docker versions match the prerequisites.
- Reinstall dependencies if necessary:
    pipenv install

____________________________________________________________________________________________________________________________________________________

###### Why This Project Matters
By predicting gym class attendance, GoalZone can:
- Reduce overcrowding in popular classes.
- Allocate gym space more efficiently.
- Enhance member experience by ensuring space availability.
