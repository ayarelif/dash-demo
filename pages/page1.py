import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# App import from this app
from app import app

# Imports for model
import pickle
import numpy as np
# import category_encoders as ce
import sklearn
# from sklearn.impute import SimpleImputer
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.pipeline import make_pipeline
# from sklearn.preprocessing import StandardScaler

# Instantiate the model
from joblib import load
#with open("./assets/model.pkl","rb") as f:
#  pipeline = pickle.load(f)
"""
    Page 1
"""

column_1 = dbc.Col([
    dcc.Markdown(
        """
            This is Column One!
        """
    )],
    md=4)

column_2 = dbc.Col([
    dcc.Markdown(
        """
            This is Column Two!
        """
    )],
    md=4)

column_3 = dbc.Col([
    dcc.Markdown(
        """
            This is Column Three!
        """
    )],
    md=4)

# Create the grid layout with these elements
layout = dbc.Row([column_1,
                  column_2,
                  column_3])

# END

