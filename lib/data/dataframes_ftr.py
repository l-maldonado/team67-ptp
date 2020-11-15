"""
File to import csv file in data dir and convert into dataframe
"""
import pandas as pd
import numpy as np
import feather
# from app import cache


# Import payer_id and merchant_id for recommendation system
filename1 = "data/bdsita.feather"
# @cache.memoize(timeout=120)
def get_db(filename=filename1):
    df_x = feather.read_dataframe(filename1)
    df_x.rename(
        columns={"transaction_payer_id": "user",
                "merchant_id": "item"}, inplace=True
    )
    return df_x


#filename2 = "data/cluster2.feather"
# @cache.memoize(timeout=120)
def get_df(filename):
    # Export cluster file for recommendation system
    df_c = feather.read_dataframe(filename)
    return df_c
