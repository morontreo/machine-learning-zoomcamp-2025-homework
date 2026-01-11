#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import pickle
import sklearn

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import make_pipeline



print(f'pandas=={pd.__version__}')
print(f'numpy=={np.__version__}')
print(f'sklearn=={sklearn.__version__}')

def load_data():
    data_url = 'https://raw.githubusercontent.com/morontreo/machine-learning-zoomcamp-2025-homework/refs/heads/main/midterm/water_potability.csv'

    df = pd.read_csv(data_url)
    # shuffle data
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    df.columns = df.columns.str.lower().str.replace(' ', '_')

    #Filling the columns with NaN with the median
    for col in ['ph', 'sulfate', 'trihalomethanes']:
        df[col] = df[col].fillna(df[col].median())

    return df

def train_model(df):
    #Defining all columns required for training
    df_columns_for_training=['ph','hardness','solids','chloramines','sulfate','conductivity','organic_carbon','trihalomethanes','turbidity']

    #Defining y_train
    y_train = df.potability
    train_dict = df[df_columns_for_training].to_dict(orient='records')

    # Creating a pipeline
    pipeline = make_pipeline(
        DictVectorizer(),
        RandomForestClassifier(n_estimators=200,
                                max_depth=10,
                                min_samples_leaf=1,
                                random_state=42)
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



