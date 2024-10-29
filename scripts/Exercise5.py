
import os
import pandas as pd
import re


# Identify resources folder
os.chdir("resources")

# Function to Load data from CSV
orders = pd.read_csv("orders.csv", sep=';')

# Function to normalize company name
def normalize_company_name(name):
    # Change names to uppercase
    name = name.upper()
    # Regex to remove '.', ',' and extra spaces
    name = re.sub(r"[.,]|\s+", " ", name).strip() 
    return name

orders['company_name'] = orders['company_name'].apply(normalize_company_name)

# Function to get saleswoners list
def get_salesowners(salesowners_column):
    salesowners = []
    for entry in salesowners_column:
        salesowners += entry.split(', ')  

    # Remove duplicates and sort the list alphabetically
    unique_salesowners = sorted(set(salesowners))
    return ', '.join(unique_salesowners)

# Funcion to get the most repeated company name
def get_company_name(company):
    return company.value_counts().idxmax()

# Group by 'company_id' with their corresponding company_name and salesowners list
df_3 = (
    orders.groupby('company_id')
    .agg({
        'company_name': get_company_name,  
        'salesowners': get_salesowners
    })
    .reset_index()
)

# Rename column name
df_3 = df_3.rename(columns={'salesowners': 'list_salesowners'})

print(df_3.to_string())