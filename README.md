# Loan Approval Automation Using MongoDB and PyMongo

This project demonstrates the implementation of a loan approval system that utilizes MongoDB for distributed data storage and management, and PyMongo for database operations. The project aims to automate the assessment of loan eligibility using customer details from online applications.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Connecting to MongoDB](#connecting-to-mongodb)
  - [CRUD Operations](#crud-operations)
  - [Data Preparation](#data-preparation)
- [Web Application Deployment](#web-application-deployment)
- [Technologies Used](#technologies-used)
- [License](#license)

## Project Overview

The loan approval system aims to automate the loan eligibility assessment process in real-time using customer details such as gender, marital status, education, dependents, income, loan amount, credit history, and more. The project includes the following key components:
1. **Problem Definition**: Automating loan eligibility assessment.
2. **Dataset Features**: Detailed feature description of the dataset used.
3. **Entity-Relationship Diagram (ERD)**: Visual representation of the database schema.
4. **Data Preprocessing**: Steps taken to preprocess the data.
5. **Data Visualization**: Visual analysis of the data.
6. **Building ML Model**: Training and evaluation of the machine learning model.
7. **Model Evaluation**: Metrics and methods used to evaluate the model.
8. **Web Application Deployment**: Steps to deploy the model as a web application.
9. **Testing and Results**: Testing the web application and presenting the results.

## Installation

To run this project, ensure you have the following installed:

- Python 3.x
- MongoDB
- Required Python libraries:
  - pymongo
  - gridfs
  - numpy
  - pandas
  - matplotlib
  - seaborn
  - scikit-learn

Install the required Python libraries using the following command:

```bash
pip install pymongo gridfs numpy pandas matplotlib seaborn scikit-learn
```

## Usage

### Connecting to MongoDB

The project demonstrates how to connect to a MongoDB instance and set up the database and collection for storing and managing data.

### CRUD Operations

The project includes functions for inserting, updating, and deleting data in MongoDB, ensuring efficient management of the dataset.

### Data Preparation

The data preparation phase involves cleaning and preprocessing the dataset, handling missing values, and encoding categorical features. This step ensures that the data is in the right format for training the machine learning model.

## Web Application Deployment

The trained machine learning model is deployed as a web application using Streamlit. The web app includes functionalities for:
- Connecting to MongoDB.
- Loading the machine learning model.
- Performing CRUD operations and making predictions.
- Designing user-friendly input fields and interface for user interaction.

## Technologies Used

- **MongoDB**: NoSQL database for storing and managing large datasets.
- **PyMongo**: Python library for interacting with MongoDB.
- **GridFS**: MongoDB specification for storing and retrieving large files.
- **Streamlit**: Framework for deploying the machine learning model as a web application.
- **Scikit-learn**: Machine learning library for training and evaluating models.
- **Pandas**: Data manipulation and analysis library.
- **Matplotlib and Seaborn**: Libraries for data visualization.

# sample of website
<img src="sample 1.png" />
<img src="sample 2.png" />

# Link for Testing Webpage :

- https://drive.google.com/file/d/1o0-Bz668aGf-j6e5yh-qqacz0cAoIKMH/view?usp=sharing 

