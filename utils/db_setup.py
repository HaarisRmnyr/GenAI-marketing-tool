import sqlite3
import pandas as pd

def create_db_and_table():

   connect = sqlite3.connect('genAI-marketing-tool.db')
   cursor = connect.cursor()

   cursor.execute('''
               CREATE TABLE IF NOT EXISTS campaigns(
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  impressions INTEGER,
                  clicks INTEGER,
                  conversions INTEGER
                  )
   ''')


   df = pd.read_sql_query("SELECT * FROM campaigns", connect)
   print(df)



