import yaml
import pandas as pd
from sqlalchemy import create_engine
import os

def load_credentials(filepath='credentials.yaml'):
     with open(filepath, 'r') as file:
        credentials = yaml.safe_load(file)
     return credentials
    

class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials
        self.host = credentials.get('RDS_HOST')
        self.port = credentials.get('RDS_PORT')
        self.username = credentials.get('RDS_USER')
        self.password = credentials.get('RDS_PASSWORD')
        self.database = credentials.get('RDS_DATABASE')
    
    def create_engine(self):
        user = self.username
        password = self.password
        host = self.host
        port = self.port
        database = self.database 
        connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
        engine = create_engine(connection_string)
        return engine    

    def get_data(self, table_name='loan_payments'):
         engine = self.create_engine()
         query = f"SELECT * FROM {table_name}"
         print(f"Executing query: {query}")
         df = pd.read_sql(query, engine)
         return df   
                    
        

    def save_to_csv(self, df, filename='loan_payments_2.csv'):
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
           


if __name__ == '__main__':
    
    credentials = load_credentials('credentials.yaml')
    db_connector = RDSDatabaseConnector(credentials)
    data = db_connector.get_data('loan_payments')
    db_connector.save_to_csv(data, 'loan_payments_3.csv')
   