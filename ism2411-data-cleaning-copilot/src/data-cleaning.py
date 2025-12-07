import pandas as pd
import numpy as np

raw_data_df = pd.read_csv('sales_data_raw.csv')

# Clean column names
def clean_column_names(raw_data_df):
    cleaned_column_names = raw_data_df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace(r'[^\w\s]', '', regex=True)
    raw_data_df.columns = cleaned_column_names 
    return raw_data_df
