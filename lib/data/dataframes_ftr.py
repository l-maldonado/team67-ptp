"""
File to import csv file in data dir and convert into dataframe
"""
import pandas as pd
import numpy as np
import feather

# Import payer_id and merchant_id for recommendation system
filename1 = "data/bdsita.feather"
df_x = feather.read_dataframe(filename1)
df_x.rename(
    columns={"transaction_payer_id": "user",
             "merchant_id": "item"}, inplace=True
)
df_x

# Export cluster file for recommendation system
filename2 = "data/cluster2.feather"
df_c = feather.read_dataframe(filename2)
df_c

cl_0 = df_c[df_c['cluster_predicted'] == 0]
cl_1 = df_c[df_c['cluster_predicted'] == 1]
