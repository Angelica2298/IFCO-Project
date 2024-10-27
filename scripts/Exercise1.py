import pandas as pd
import os
import json

# Test 1:  Distribution of Crate Type per Company #
###################################################

# Identify resources folder
os.chdir("resources")

# Function to Load data from CSV
def load_data(file_path):
    return pd.read_csv(file_path, sep=';')

# Function to calculate distribution of CRATES as requested
def get_crate_distribution(df):
    distribution = df.groupby(['company_name', 'crate_type']).size().reset_index(name='order_count')
    return distribution

orders_df = load_data("orders.csv")
distribution = get_crate_distribution(orders_df)
print(distribution)

