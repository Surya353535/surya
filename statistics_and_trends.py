"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    fig, ax = plt.subplots()
    """
    Plots a relational plot using seaborn to show relationships between variables.
    This plot helps in visualizing the relationship between two numerical variables.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df, x='filter_age_days', y='efficiency', ax=ax)
    ax.set_title("Relational Plot between Filter Age and Efficiency")
    plt.savefig('relational_plot.png')
    return


def plot_categorical_plot(df):
    """Plots a categorical plot to visualize the distribution of categorical data.
    This helps in comparing categories of filters based on a numerical variable, such as pressure drop.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(data=df, x='filter_class', y='pressure_drop_pa', ax=ax)
    ax.set_title("Categorical Plot of Pressure Drop by Filter Class")
    plt.savefig('categorical_plot.png')
    return


def plot_statistical_plot(df):
    """
    Plots a statistical plot such as a histogram or distribution plot for a numerical column.
    The plot visualizes the distribution and spread of the numerical data.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(df['efficiency'], kde=True, ax=ax, color='blue', bins=20)
    ax.set_title("Statistical Plot of Efficiency Distribution")
    plt.savefig('statistical_plot.png')
    return


def statistical_analysis(df, col: str):
    """
    Performs statistical analysis on a selected column and calculates the mean, 
    standard deviation, skewness, and excess kurtosis.
    
    Parameters:
    - df (DataFrame): The dataset containing the data.
    - col (str): The column name for which to perform the analysis.
    
    Returns:
    - tuple: (mean, standard deviation, skewness, excess kurtosis)
    """
    mean = df[col].mean()
    stddev = df[col].std()
    skew = df[col].skew()
    excess_kurtosis = df[col].kurtosis() - 3
    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
    """
    Preprocess the data by handling missing values, generating basic statistics, 
    and possibly filtering or transforming the data.
    
    Parameters:
    - df (DataFrame): The raw dataset.
    
    Returns:
    - DataFrame: The cleaned or preprocessed dataset.
    """
    # You should preprocess your data in this function and
    print(df.corr())
    print(df.tail())
    print(df.head())
    print(df.describe())
    
    # make use of quick features such as 'describe', 'head/tail' and 'corr'.
    return df


def writing(moments, col):
    """
    Writes the statistical results to the console.
    
    Parameters:
    - moments (tuple): Statistical moments including mean, stddev, skewness, and excess kurtosis.
    - col (str): The column name for which the analysis was performed.
    """
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')
    # Delete the following options as appropriate for your data.
    # Not skewed and mesokurtic can be defined with asymmetries <-2 or >2.
    print('The data was right/left/not skewed and platy/meso/leptokurtic.')
    return

def main():
    """
    Main function to load the dataset, preprocess it, generate plots, perform statistical analysis, 
    and output the results.
    """
    df = pd.read_csv('data.csv')
    df = preprocessing(df)
    col = 'efficiency'
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return


if __name__ == '__main__':
    main()
