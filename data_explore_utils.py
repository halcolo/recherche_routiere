import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification # To test if RandomForestClassifier is imported correctly
from sklearn.metrics import f1_score
from data_cleaning_utils import filter_columns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, precision_recall_curve, auc
import itertools

def generate_sample_data(df, yColumn="grav"):
    
    if(df[yColumn].isnull().any()):
        raise ValueError("missing values in column '" + yColumn + "'")
    y = df[yColumn].to_list()
    
    # getting all the columns
    new_cols = set(df.columns)
    # removing the desired column
    new_cols.remove(yColumn)
    new_cols = list(new_cols)
    X = df[new_cols]
    return X.to_numpy(), y