#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import pickle
import sklearn

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

print(f'pandas=={pd.__version__}')
print(f'numpy=={np.__version__}')
print(f'sklearn=={sklearn.__version__}')

def load_data():
    data_url = 'https://raw.githubusercontent.com/morontreo/machine-learning-zoomcamp-2025-homework/refs/heads/main/capstone-02/higher-education-predictors-of-student-retention.csv'

    df = pd.read_csv(data_url)
    
    #Setting all columns to lower case and removing spaces
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    #Removing the Enrolled record to focus on Dropout or Graduate
    df = df[df['target'] != 'Enrolled']
    
    #Encode the target value
    order_map = {'Dropout': 0, 'Graduate': 1}
    df['target'] = df['target'].map(order_map)

    return df

def train_model(df):
    #Defining all columns required for training
    df_columns_for_training=['marital_status', 'application_mode', 'application_order', 'course', 'daytime/evening_attendance', 'previous_qualification', 
                         'nacionality', "mother's_qualification", "father's_qualification", "mother's_occupation", "father's_occupation", 'displaced',
                         'educational_special_needs', 'debtor', 'tuition_fees_up_to_date', 'gender', 'scholarship_holder', 'age_at_enrollment', 
                         'international', 'curricular_units_1st_sem_(credited)', 'curricular_units_1st_sem_(enrolled)', 
                         'curricular_units_1st_sem_(evaluations)', 'curricular_units_1st_sem_(approved)', 'curricular_units_1st_sem_(grade)', 
                         'curricular_units_1st_sem_(without_evaluations)', 'curricular_units_2nd_sem_(credited)', 'curricular_units_2nd_sem_(enrolled)',
                         'curricular_units_2nd_sem_(evaluations)', 'curricular_units_2nd_sem_(approved)', 'curricular_units_2nd_sem_(grade)', 
                         'curricular_units_2nd_sem_(without_evaluations)', 'unemployment_rate', 'inflation_rate', 'gdp']

    #Defining y_train
    y_train = df.target
    train_dict = df[df_columns_for_training].to_dict(orient='records')

    # Creating a pipeline
    pipeline = make_pipeline(
        DictVectorizer(),
        LogisticRegression(solver='liblinear', C=1.0, max_iter=1000, random_state=42)
    )

    pipeline.fit(train_dict, y_train)

    return pipeline

def save_model(pipeline, output_file):
    # Saving Model with pickle
    with open('model.bin', 'wb') as f_out:
        pickle.dump(pipeline, f_out)

df = load_data()
pipeline = train_model(df)
save_model(pipeline, 'model.bin')

print('Model saved to model.bin')



