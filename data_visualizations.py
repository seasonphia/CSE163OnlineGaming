'''
Kiho Noh and Sophia Wei
CSE163 Final Project: Online Gaming
'''

# Will need to comment the programs and methods eventually

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import data_processing
import machine_learning

sns.set()


def narcissism_gaming_hours(df):
    filtered_df = df[['Hours', 'Narcissism']]
    realistic_weekly_hours = df['Hours'] <= 168
    filtered_df = filtered_df[realistic_weekly_hours]

    plt.figure()
    sns.relplot(x='Hours', y='Narcissism', hue='Narcissism',
                style='Narcissism',
                data=filtered_df).set(yticks=[1, 2, 3, 4, 5])

    plt.title('Narcissism & Weekly Online Gaming')
    plt.xlabel('Weekly Gaming Hours')
    plt.ylabel('Narcissistic Tendencies')
    plt.savefig('onlinegamingnarcissism.png', bbox_inches='tight')


def narcissism_over_20_hours(df):
    filtered_df = df[['Hours', 'Narcissism']]
    over_20_hours = (df['Hours'] > 20) & (df['Hours'] <= 168)
    filtered_df = filtered_df[over_20_hours]

    plt.figure()
    sns.set_theme(style="whitegrid")
    sns.regplot(x='Hours', y='Narcissism', color='red', fit_reg = True,
                ci = 95, scatter_kws={'s': 5},
                data=filtered_df).set(xticks=[0, 25, 50, 75, 100,
                125, 150, 175])

    plt.title('Narcissism & Excessive Online Gaming')
    plt.xlabel('Weekly Gaming Hours')
    plt.ylabel('Narcissistic Tendencies')
    plt.savefig('excessivegamingnarcissism.png', bbox_inches='tight')


def narcissism_mental_health(df, mental_health):
    filtered_df = df[['Narcissism', 'GAD_T', 'SWL_T', 'SPIN_T']]
    high_narcissism = (filtered_df['Narcissism'] == 4) | \
                        (filtered_df['Narcissism'] == 5)
    factor = filtered_df[mental_health]
    filtered_df = filtered_df[high_narcissism & factor]

    plt.figure()
    sns.set_theme(style="whitegrid")
    sns.boxplot(x='Narcissism', y=mental_health, hue='Narcissism',
                color='green', saturation=0.7, data=filtered_df)
    sns.swarmplot(x='Narcissism', y=mental_health, hue='Narcissism',
                color='pink', size=1, data=filtered_df)

    plt.title(f'Narcissism & {mental_health}')
    if (mental_health == 'GAD_T'):
        mental_health = 'Generalized Anxiety Disorder'
    elif (mental_health == 'SWL_T'):
        mental_health = 'Satisfaction With Life'
    else:
        mental_health = 'Social Phobia Inventory Score'

    plt.xlabel('High Narcissistic Tendencies')
    plt.ylabel(f'{mental_health}')
    plt.savefig(f'{mental_health}.png', bbox_inches='tight')


def main():
    df = pd.read_csv("GamingStudy_data.csv")
    data = data_processing.process_data(df)
    narcissism_gaming_hours(data)
    narcissism_over_20_hours(data)
    narcissism_mental_health(data, 'GAD_T')
    narcissism_mental_health(data, 'SPIN_T')
    narcissism_mental_health(data, 'SWL_T')


if __name__ == '__main__':
    main()