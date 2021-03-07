'''
Kiho Noh and Sophia Wei
CSE163 Final Project: Online Gaming
'''

# Will need to comment the programs and methods eventually


import pandas as pd


def process_data(df):
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


def main():
    df = pd.read_csv("GamingStudy_data.csv")
    data = process_data(df)


if __name__ == '__main__':
    main()