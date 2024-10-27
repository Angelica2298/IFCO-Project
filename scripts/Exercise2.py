import os
import pandas as pd
import json

# Test 2: DataFrame of Orders with Full Name of the Contact #
##############################################################

# Identify resources folder
os.chdir("resources")

# Function to Load data from CSV
orders = pd.read_csv("orders.csv", sep=';')

#df_orders = pd.read_csv('Orders.csv')

## Function that retreives full name information
def get_full_name(contact_data):
    try:
        # Check null values
        if pd.isna(contact_data) or not isinstance(contact_data, str):
            return 'John Doe'

        # Replace single quotes with double quotes
        data = json.loads(contact_data.replace("'", '"'))
        
        # Check if list or not
        if isinstance(data, list) and len(data) > 0:
            contact_name = data[0].get('contact_name', 'John')
            contact_surname = data[0].get('contact_surname', 'Doe')
            #return f"{contact_name} {contact_surname}"
        else:
            contact_name = data.get('contact_name', 'John')
            contact_surname = data.get('contact_surname', 'Doe')

        return f"{contact_name} {contact_surname}"
    except (IndexError, ValueError):
        return 'John Doe'

# creation of DataFrame with order ID and contact full Name
df_1 = pd.DataFrame({
    'order_id': orders['order_id'],
    'contact_full_name': orders['contact_data'].apply(get_full_name)
})

print(df_1)