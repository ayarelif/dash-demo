import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# App import from this app
from app import app

# Imports for model

import numpy as np
import category_encoders as ce
import sklearn
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from model import model


"""
    Page 1
"""

column_1 = dbc.Col([
    dcc.Markdown(
        """
            This is Column One!
        """
    ),dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC'
    ),],
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

