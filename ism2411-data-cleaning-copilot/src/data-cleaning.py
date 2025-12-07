import pandas as pd
import numpy as np

raw_data_df = pd.read_csv('sales_data_raw.csv')

# Clean column names
def clean_column_names(raw_data_df):
    cleaned_column_names = raw_data_df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace(r'[^\w\s]', '', regex=True)
    raw_data_df.columns = cleaned_column_names 
    return raw_data_df

# Remove invalid rows
def remove_invalid_rows(raw_data_df):
    raw_data_df = raw_data_df.dropna(subset=['order_id', 'customer_id', 'sales_amount'])
    raw_data_df = raw_data_df[cleaned_data_df['sales_amount'] >= 0]
    return raw_data_df