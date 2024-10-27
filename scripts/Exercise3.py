import os
import pandas as pd
import json

# Test 3: DataFrame of Orders with Contact Address #
##############################################################

# Identify resources folder
os.chdir("resources")

# Function to Load data from CSV
orders = pd.read_csv("orders.csv", sep=';')

## Function that retreives full address information
def get_full_address(contact_data):
    try:
        # Check null values
        if pd.isna(contact_data) or not isinstance(contact_data, str):
            return 'Unknown, UNK00'

        # Replace single quotes with double quotes
        data = json.loads(contact_data.replace("'", '"'))
        
        # Check if list or not
        if isinstance(data, list) and len(data) > 0:
            city = data[0].get('city', 'Unknown')
            cp = data[0].get('cp', 'UNK00')
        else:
            city = data.get('city', 'Unknown')
            cp = data.get('cp', 'UNK00')

        return f"{city}, {cp}"
    except (IndexError, ValueError):
        return 'Unknown, UNK00'

# creation of DataFrame with order ID and contact full Name
df_2 = pd.DataFrame({
    'order_id': orders['order_id'],
    'contact_address': orders['contact_data'].apply(get_full_address)
})

print(df_2.to_string())