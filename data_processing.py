'''
Kiho Noh and Sophia Wei
CSE163 Final Project: Online Gaming
This program uses the pandas library to implement the data processing method
in order to read through an Online Gaming dataset CSV file and parse down to
the columns of interest.
'''


import pandas as pd


def process_data(df):
    '''
    This function takes in a dataframe, filters it and returns a new
    dataframe with the columns of interest.
    '''
    filtered_df = df.loc[:, ["GAD1", "GAD2", "GAD3", "GAD4",
                             "GAD5", "GAD6", "GAD7", "GADE", "SWL1",
                             "SWL2", "SWL3", "SWL4", "SWL5", 'Hours',
                             'SPIN1', 'SPIN2', 'SPIN3', 'SPIN4',
                             'SPIN5', 'SPIN6', 'SPIN7', 'SPIN8',
                             'SPIN9', 'SPIN10', 'SPIN11', 'SPIN12',
                             'SPIN13', 'SPIN14', 'SPIN15', 'SPIN16',
                             'SPIN17', 'Narcissism', 'Age', 'Work',
                             'GAD_T', 'SWL_T', 'SPIN_T']]
    filtered_df = filtered_df.dropna()

    return filtered_df