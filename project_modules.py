import pandas as pd
import numpy as np
import seaborn as sns


def series_to_list(data,columns=None):
    if columns == None:
        columns = data.columns

    return list(data[columns].values)

def find_outliers_df(data,method="std"):
    if method == 'std':
        outliers = dict()
        for column in data.columns:
            outliers[column] = data[data[column].std > 3]    
    return outliers


def find_outliers_series(series):
    outliers = series[series>(series.std()*3)]

    return outliers







