# IBM-Project-2226-1658467109
### TEAM ID : PNT2022TMID17830
Deep Learning Fundus Image Analysis for Early Detection of Diabetic Retinopathy

## Pre Requisites
Install the following python packages
  * pip install numpy
  * pip install pandas
  * pip install tensorflow==2.3.2
  * pip install keras==2.3.1
  * pip install Flask

## Prior Knowledge
You must have prior knowledge of following topics to complete this project.
  * Deep Learning Concepts 
  * CNN
  * VGG16
  * ResNet-50
  * Inception-V3
  * Xception
  * Flask: 
    *  *Flask is a popular Python web framework, meaning it is a third-party Python library used for developing web applications.*

## Project Objectives
Know fundamental concepts and techniques of transfer learning like Xception.
Gain a broad understanding of image data.
Know how to pre-process/clean the data using different data pre-processing techniques.
Know how to build a web application using the Flask framework.

## Project Flow
The user interacts with the UI (User Interface) to choose the image.
The chosen image analyzed by the model which is integrated with flask application.
The Xception Model analyzes the image, then the prediction is showcased on the Flask UI.

To accomplish this
 1. Data Collection
 2. Data Preprocessing
 3. Model Building
 4. Cloudant DB
 5. Application Building

## Project Structure
Create project structure as shown below

![Structure](https://lh5.googleusercontent.com/YhUnQA5GR__bgT0Gr3-mUDYeec2NN1hLVQONvPw9Dxgv0PJptlw34CcP-pdWn_VYTcMIkOFsH5zl4tMKZ6v8s7sD0V_NS5EuKsms_M2YlQlGk1mMsoiUpWpi-LfR6A)

## Dataset link

[Kaggle Dataset link](https://www.kaggle.com/datasets/arbethi/diabetic-retinopathy-level-detection?select=preprocessed+dataset)

Download the dataset
Use CNN and add dense layer
Train and save the model

## Cloud
 * Register and login to cloud
 * Create service instance and service essentials
 * Launch cloudant DB and create database
 
## Application Building
  -> In this phase we will build a simple HTML page that runs python code using flask
  
#### Finally register the model in IBM Cloud and train the model

### Using the virtual env
  * Unzip the retino-env.zip to your final deliverables 
  * then activate the bat (retino-env\Scripts\activate.bat
  * run your app.py file
