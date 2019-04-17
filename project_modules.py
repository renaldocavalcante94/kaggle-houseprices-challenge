import pandas as pd
import numpy as np
import seaborn as sns


def series_to_list(data,columns=None):
    if columns == None:
        columns = data.columns

    return list(data[columns].values)

        
