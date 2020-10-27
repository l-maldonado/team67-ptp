import pandas as pd
import feather

preprocess_mf = __import__("preprocessor").preprocess_mf
filename = "C:/Users/anemi/OneDrive/Escritorio/dataframes/placetopayDB4.ftr"
preprocess_mf(filename, "isic_section_name", "transaction_processing_amount")
