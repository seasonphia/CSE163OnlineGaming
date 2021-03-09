'''
Kiho Noh and Sophia Wei
CSE163 Final Project: Online Gaming
'''

# Will need to comment the programs and methods eventually


from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import data_processing


def ml_narcissism(df):
    filtered_df = df[['Hours', 'Narcissism', 'GAD_T', 'SWL_T', 'SPIN_T']]
    over_20_hours = filtered_df['Hours'] > 20
    filtered_df = filtered_df[over_20_hours]

    # Features: Weekly hours of online gaming & Total SWL score,
    # Total GAD score & Total SPIN score
    # Label: degree exhibiting narcissistic tendencies
    features = filtered_df.loc[:, filtered_df.columns != 'Narcissism']
    swlhours_feature = filtered_df.loc[:, ['Hours', 'SWL_T']]
    gadspin_feature = filtered_df.loc[:, ['GAD_T', 'SPIN_T']]
    labels = filtered_df['Narcissism']

    # Split up the data into Training Set & Testing Set
    features_train1, features_test1, labels_train1, labels_test1 = \
        train_test_split(features, labels, test_size = 0.3)

    features_train2, features_test2, labels_train2, labels_test2 = \
        train_test_split(swlhours_feature, labels, test_size = 0.3)

    features_train3, features_test3, labels_train3, labels_test3 = \
        train_test_split(gadspin_feature, labels, test_size = 0.3)

    # Fit the model onto the data
    model1 = DecisionTreeRegressor()
    model1.fit(features_train1, labels_train1)

    model2 = DecisionTreeRegressor()
    model2.fit(features_train2, labels_train2)

    model3 = DecisionTreeRegressor()
    model3.fit(features_train3, labels_train3)

    # Find Predictions and Compute error on Training Set and on Testing Set
    predictions = model1.predict(features_test1)
    error = mean_squared_error(labels_test1, predictions)

    swlhours_predictions = model2.predict(features_test2)
    swlhours_error = mean_squared_error(labels_test2, swlhours_predictions)

    gadspin_predictions = model3.predict(features_test3)
    gadspin_error = mean_squared_error(labels_test3, gadspin_predictions)

    print(f'Error in Narcissism prediction with Hours input: {error:.2f}\nError in Narcissism prediction with GAD and SPIN scores input: {swlhours_error:.2f}\nError in Narcissism prediction with SWL score inputs: {gadspin_error:.2f}')
    return error, swlhours_error, gadspin_error


def main():
    df = pd.read_csv("GamingStudy_data.csv")
    data = data_processing.process_data(df)
    ml_narcissism(data)


if __name__ == '__main__':
    main()