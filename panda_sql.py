from exo_panda import data
"""
Load employee data from a pandas DataFrame into a MySQL database.

This module connects to a MySQL database using SQLAlchemy and writes
employee data to the 'employees' table. The connection uses PyMySQL
as the driver.

The data is loaded with the following behavior:
- Table name: 'employees'
- If the table exists: it will be replaced (all existing data removed)
- DataFrame index: not written to the database

Prerequisites:
- MySQL server running on localhost:3306
- 'company' database exists
- Valid credentials (root user with password)
- Required packages: pandas, sqlalchemy, pymysql

Note:
    The connection credentials are hardcoded in this file.
    Consider using environment variables or configuration files
    for sensitive information in production environments.
"""
import pandas as pd
from sqlalchemy import create_engine
connection_string = "mysql+pymysql://root:qyk5bb@localhost:3306/company"
engine = create_engine(connection_string)
data.to_sql(
    name='employees', 
    con=engine,
    if_exists='replace',  
    index=False
)
