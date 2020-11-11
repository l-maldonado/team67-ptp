import pandas as pd
import numpy as np
from IPython.display import Image

# ---helper modules---

import io
import os

# ---loading modules---
import feather


def preprocess_var(bd, var):
    """Preprocessor a single variable to csv"""
    filepath_sv = f"team67-ptp/data/{var}.csv"
    filepath = bd
    data = feather.read_dataframe(filepath)
    df = data.copy()
    df2 = df[var]
    df2 = df2.to_frame()
    if df2[var].dtype is "category":
        df2[var] = df2[var].astype("category").cat.codes
        filename = filepath_sv
        df2.to_csv(filename, index=False)
        print("Succesfully exported to csv")
    else:
        filename = filepath_sv
        df2.to_csv(filename, index=False)
        print("Succesfully exported to csv")


def preprocess_mul(bd, var1, var2):
    """Preprocessor two variables to csv"""
    filepath_mv = f"team67-ptp/data/{var1}_{var2}.csv"
    filepath = bd
    data = feather.read_dataframe(filepath)
    df = data.copy()
    df2 = df[[var1, var2]]
    if df2[var1].dtype is "category" and df2[var2].dtype is "category":
        df2[var1] = df2[var1].astype("category").cat.codes
        df2[var2] = df2[var2].astype("category").cat.codes
        filename = filepath_mv
        df2.to_csv(filename, index=False, encoding="utf-16")
        print("Succesfully exported to csv")
    elif df2[var1].dtype is "category" and df2[var2].dtype is not "category":
        df2[var1] = df2[var1].astype("category").cat.codes
        filename = filepath_mv
        df2.to_csv(filename, index=False, encoding="utf-16")
        print("Succesfully exported to csv")
    elif df2[var1].dtype is not "category" and df2[var2].dtype is "category":
        df2[var2] = df2[var2].astype("category").cat.codes
        filename = filepath_mv
        df2.to_csv(filename, index=False, encoding="utf-16")
        print("Succesfully exported to csv")
    else:
        filename = filepath_mv
        df2.to_csv(filename, index=False, encoding="utf-16")
        print("Succesfully exported to csv")


def preprocess_sf(bd, var):
    """Preprocessor a single variable to feather"""
    filepath_svf = f"team67-ptp/data/{var}.ftr"
    filepath = bd
    data = feather.read_dataframe(filepath)
    df = data.copy()
    df2 = df[var]
    df2 = df2.to_frame()
    if df2[var].dtype is "category":
        df2[var] = df2[var].astype("category").cat.codes
        filename = filepath_svf
        df2.to_feather(filename)
        print("Succesfully exported to feather")
    else:
        filename = filepath_svf
        df2.to_feather(filename)
        print("Succesfully exported to feather")


def preprocess_mf(bd, var1, var2):
    """Preprocessor two variables to feather"""
    filepath_mvf = f"team67-ptp/data/{var1}_{var2}.ftr"
    filepath = bd
    data = feather.read_dataframe(filepath)
    df = data.copy()
    df2 = df[[var1, var2]]
    if df2[var1].dtype is "category" and df2[var2].dtype is "category":
        df2[var1] = df2[var1].astype("category").cat.codes
        df2[var2] = df2[var2].astype("category").cat.codes
        filename = filepath_mvf
        df2.to_csv(filename)
        print("Succesfully exported to feather")
    elif df2[var1].dtype is "category" and df2[var2].dtype is not "category":
        df2[var1] = df2[var1].astype("category").cat.codes
        filename = filepath_mvf
        df2.to_csv(filename)
        print("Succesfully exported to feather")
    elif df2[var1].dtype is not "category" and df2[var2].dtype is "category":
        df2[var2] = df2[var2].astype("category").cat.codes
        filename = filepath_mvf
        df2.to_feather(filename)
        print("Succesfully exported to feather")
    else:
        filename = filepath_mvf
        df2.to_feather(filename)
        print("Succesfully exported to feather")


def preprocess_mf3(bd, var1, var2, var3):
    """Preprocessor a three variables to feather"""
    filepath_mvf = f"team67-ptp/data/{var1}_{var2}_{var3}.ftr"
    filepath = bd
    data = feather.read_dataframe(filepath)
    df = data.copy()
    df2 = df[[var1, var2, var3]]
    if (
        df2[var1].dtype is "category"
        and df2[var2].dtype is "category"
        and df2[var3].dtype is "category"
    ):
        df2[var1] = df2[var1].astype("category").cat.codes
        df2[var2] = df2[var2].astype("category").cat.codes
        df2[var3] = df2[var3].astype("category").cat.codes
        filename = filepath_mvf
        df2.to_csv(filename)
        print("Succesfully exported to feather")
    elif (
        df2[var1].dtype is "category"
        and df2[var2].dtype is not "category"
        and df2[var3].dtype is not "category"
    ):
        df2[var1] = df2[var1].astype("category").cat.codes
        filename = filepath_mvf
        df2.to_csv(filename)
        print("Succesfully exported to feather")
    elif (
        df2[var1].dtype is not "category"
        and df2[var2].dtype is "category"
        and df2[var3].dtype is "category"
    ):
        df2[var2] = df2[var2].astype("category").cat.codes
        filename = filepath_mvf
        df2.to_feather(filename)
        print("Succesfully exported to feather")
    else:
        filename = filepath_mvf
        df2.to_feather(filename)
        print("Succesfully exported to feather")
