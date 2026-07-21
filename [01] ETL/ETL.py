import pandas as pd
import pyodbc
from sqlalchemy import create_engine
import urllib
import os

# customer table
cust = pd.read_csv(r'/Users/amanraj/Data Analytics Projects/Global-ELectronics-Rettailer-sales-and-customer-Insights/[01] ETL/Cleaned Datasets/cleaned_customers.csv')
# drop Unnamed: 0 
cust = cust.drop('Unnamed: 0', axis=1)

# sales table
sales = pd.read_csv(r'/Users/amanraj/Data Analytics Projects/Global-ELectronics-Rettailer-sales-and-customer-Insights/[01] ETL/Cleaned Datasets/cleaned_sales.csv')
# drop Unnamed: 0 
sales = sales.drop('Unnamed: 0', axis=1)

# stores table
stores = pd.read_csv(r'C/Users/amanraj/Data Analytics Projects/Global-ELectronics-Rettailer-sales-and-customer-Insights/[01] ETL/Cleaned Datasets/cleaned_stores.csv')
# drop Unnamed: 0 
stores = stores.drop('Unnamed: 0', axis=1)

# products table
prod = pd.read_csv(r'/Users/amanraj/Data Analytics Projects/Global-ELectronics-Rettailer-sales-and-customer-Insights/[01] ETL/Cleaned Datasets/cleaned_products.csv')
# drop Unnamed: 0 
prod = prod.drop('Unnamed: 0', axis=1)

# exchange rates table
rates = pd.read_csv(r'/Users/amanraj/Data Analytics Projects/Global-ELectronics-Rettailer-sales-and-customer-Insights/[01] ETL/Cleaned Datasets/cleaned_exchange_rates.csv')
# drop Unnamed: 0 
rates = rates.drop('Unnamed: 0', axis=1)

server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE", "Global_Electronics_Retailer")
username = os.getenv("SQL_USERNAME")
password = os.getenv("SQL_PASSWORD")
 
if not all([server, username, password]):
    raise ValueError(
        "Set SQL_SERVER, SQL_USERNAME, and SQL_PASSWORD before running this script."
    )

# create a connection string
connection_string = (
    f"mssql+pyodbc://{username}:{urllib.parse.quote_plus(password)}"
    f"@{server}/{database}?driver=ODBC+Driver+18+for+SQL+Server"
)
engine = create_engine(connection_string)

# create a dictionary of dataFrames
dataframes = {
    'customers': cust,
    'sales': sales,
    'stores': stores,
    'products': prod,
    'exchange_rates': rates
}

# load each dataframe into sql
for table_name, df in dataframes.items():
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
