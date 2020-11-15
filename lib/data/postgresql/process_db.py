"""
File to call any data from a RDS instance of postsgresql
to the application
"""

import pandas as pd
import numpy as np
import re
import io
from sqlalchemy import create_engine

host = "xxxxxxxxxxx.us-east-1.rds.amazonaws.com"
port = 5432
user = "xxxxxx"
passc = "xxxxxx"
db = "xxxxxx"

# connDB = create_engine(f"postgresql://{user}:{passc}@{host}:{port}/{db}")
# conn = connDB.raw_connection()
# cur = conn.cursor()

# df_x = pd.read_sql("SELECT * FROM payer_merchant ", connDB)
# df_x.rename(columns={"payer": "user", "merchant": "item"}, inplace=True)
# df_x
