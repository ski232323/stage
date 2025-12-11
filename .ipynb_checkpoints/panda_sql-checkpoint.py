from exo_panda import data
import pandas as pd
from sqlalchemy import create_engine
connection_string = "mysql+pymysql://root:qyk5bb@localhost:3306/company"
engine = create_engine(connection_string)
data.to_sql(
    name='employees',  # Nom de la table dans MariaDB
    con=engine,
    if_exists='replace',  # 'replace', 'append', ou 'fail'
    index=False
)