import streamlit as st
import pandas as pd
import pickle
from pymongo import MongoClient

# Connect to your MongoDB cluster
client = MongoClient("localhost", 27017)
db = client.project  # Change 'your_database_name' to your actual database name
collection = db.project  # Change 'your_collection_name' to your actual collection name

# Load the pre-trained model (replace 'best_model.pkl' with your actual pickle file)
with open('best_model.pkl', 'rb') as file:
      model = pickle.load(file)

# Define functions for CRUD operations
def insert_data_into_mongodb(data):
      collection.insert_one(data)
      st.success("Data inserted into MongoDB!")

def update_data_in_mongodb(filter_criteria, updated_data):
      collection.update_one(filter_criteria, {'$set': updated_data})
      st.success("Data updated in MongoDB!")

def delete_data_from_mongodb(filter_criteria):
      collection.delete_one(filter_criteria)
      st.success("Data deleted from MongoDB!")

# Define the Streamlit app
def main():
      # Add custom CSS styles
      st.markdown("""
      <style>
      h1 {
            color: #FF5733;
      }
      p {
            color: #808080;
      }
      h3 {
            color: #FF5733;
      }
      </style>
      """, unsafe_allow_html=True)

      st.markdown("<h1>Loan Approval Prediction</h1>", unsafe_allow_html=True)
      st.markdown("<p>This web app predicts loan approval based on applicant details.</p>", unsafe_allow_html=True)

      st.markdown("<h3>App Description</h3>", unsafe_allow_html=True)
      st.markdown("<p>This web app uses a pre-trained machine learning model to predict whether a loan application will be approved or not. It takes various applicant details as input and provides the prediction as output.</p>", unsafe_allow_html=True)

      st.markdown("<h3>Enter Applicant Details</h3>", unsafe_allow_html=True)
      with st.form("applicant_details"):
            col1, col2 = st.columns([3, 1])
            applicant_income = st.number_input('Applicant Income')
            coapplicant_income = st.number_input('Coapplicant Income')
            loan_amount_term = st.number_input('Loan Amount Term')
            credit_history = st.number_input('Credit History')
            loan_amount = st.number_input('Loan Amount')

            gender = st.selectbox('Gender', ['Male', 'Female'])
            married = st.selectbox('Marital Status', ['Yes', 'No'])
            dependents = st.selectbox('Number of Dependents', ['0', '1', '2', '3+'])
            education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
            self_employed = st.selectbox('Self Employed', ['Yes', 'No'])
            property_area = st.selectbox('Property Area', ['Urban', 'Semiurban', 'Rural'])

            gender_val = 1 if gender == 'Male' else 0
            married_val = 1 if married == 'Yes' else 0
            dependents_val = int(dependents[0]) if dependents != '3+' else 3
            education_val = 1 if education == 'Not Graduate' else 0
            self_employed_val = 1 if self_employed == 'Yes' else 0
            property_area_val = 1 if property_area == 'Semiurban' else (2 if property_area == 'Urban' else 0)

            # Create a dictionary from user inputs
            input_data = {
                  'ApplicantIncome': applicant_income,
                  'CoapplicantIncome': coapplicant_income,
                  'Loan_Amount_Term': loan_amount_term,
                  'Credit_History': credit_history,
                  'LoanAmount': loan_amount,
                  'Gender_Male': gender_val,
                  'Married_Yes': married_val,
                  'Dependents_1': 1 if dependents_val == 1 else 0,
                  'Dependents_2': 1 if dependents_val == 2 else 0,
                  'Dependents_3+': 1 if dependents_val == 3 else 0,
                  'Education_Not Graduate': education_val,
                  'Self_Employed_Yes': self_employed_val,
                  'Property_Area_Semiurban': 1 if property_area_val == 1 else 0,
                  'Property_Area_Urban': 1 if property_area_val == 2 else 0
            }

            # Prepare input data as a DataFrame for prediction
            input_df = pd.DataFrame([input_data])

            if st.form_submit_button('Predict'):
                  prediction = model.predict(input_df)
                  if prediction[0] == 0:
                        st.success(f'Prediction: Soory!, But you are not eligible for loan')
                  else:
                        st.success(f'Prediction: cograts!, You are eligible for loan')

      # Buttons for CRUD operations
      st.markdown("<h3>Actions</h3>", unsafe_allow_html=True)
      col1, col2, col3 = st.columns(3)
      with col1:
            if st.button('Create', key='create_button'):
                  insert_data_into_mongodb(input_data)
      with col2:
            if st.button('Update', key='update_button'):
                  filter_criteria = {}  # Define your filter criteria
                  updated_data = {}  # Define your updated data
                  update_data_in_mongodb(filter_criteria, updated_data)
      with col3:
            if st.button('Delete', key='delete_button'):
                  filter_criteria = {}  # Define your filter criteria
                  delete_data_from_mongodb(filter_criteria)

if __name__ == '__main__':
      main()
