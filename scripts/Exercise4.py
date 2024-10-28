import os
import pandas as pd
import json
from collections import defaultdict

# Identify resources folder
os.chdir("resources")

# Function to Load data from CSV
orders = pd.read_csv("orders.csv", sep=';')

# Load JSON
with open('invoicing_data.json') as data_Json:
    invoicing_data = json.load(data_Json)

invoicing = pd.DataFrame(invoicing_data)

df_invoicing = pd.DataFrame(invoicing.data.invoices)

# Merge filtered dataframes orders and invoicing
orders_filter = orders[['order_id','salesowners']]
invoicing_filter = df_invoicing[['orderId','grossValue']]
df = pd.merge(orders_filter, invoicing_filter, left_on='order_id', right_on='orderId')

# Conversion to euros
df['grossValue'] = df['grossValue'].astype(int) / 100  

# Function to calculate commissions
def get_commissions(row):    
    salesowners = row['salesowners']
    list_salesowners = salesowners.split(', ') # Split with ', ' because only ',' duplicate the data
    grossValue = row['grossValue']

    commissions = {}
    
    if len(list_salesowners) > 0:
        commissions[list_salesowners[0]] = grossValue * 0.06  # Main owner -> 6%
    if len(list_salesowners) > 1:
        commissions[list_salesowners[1]] = grossValue * 0.025  # Co-owner 1 -> 2.5 %
    if len(list_salesowners) > 2:
        commissions[list_salesowners[2]] = grossValue * 0.0095  # Co-owner 2 -> 095%
    
    return commissions

total_commissions = defaultdict(float)

for column, row in df.iterrows():
    commissions = get_commissions(row)
    for owner, commission in commissions.items():
        total_commissions[owner] += commission

#  DataFrame with results
df_commissions = pd.DataFrame(
    {'sales_owner': list(total_commissions.keys()),
     'commission': [round(com, 2) for com in total_commissions.values()]}
)

# DataFrame sorted in order of descending performance
df_commissions = df_commissions.sort_values(by='commission', ascending=False)

print(df_commissions)