import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_data_types(df):
    cols = df.columns
    dtypes = df.dtypes
    return pd.DataFrame({'column': cols, 'dtype': dtypes})

def get_summary_stats(df):
    m = (df.describe().T)
    m['IQR'] = m['75%'] - m['25%']
    m = m.rename(columns={'50%':'median'})
    m['na_count'] = df.isna().sum()
    m['unique_count'] = df.nunique()
    return m[['count', 'mean', 'std', 'min', 'max', 'median', 'IQR',
     'unique_count', 'na_count']]

def get_numeric_histograms(df):
    df_numeric = df.select_dtypes(include=['int64', 'float64'])
    df_numeric.hist(bins=50, figsize=(20,15))
    plt.show()

def get_numeric_boxplots(df):
    df_numeric = df.select_dtypes(include=['int64', 'float64'])
    df_numeric.boxplot(figsize=(20,15))
    plt.show()

    


