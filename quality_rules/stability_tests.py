import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

def test_statistical_stability(dataset_v1: pd.DataFrame, dataset_v2: pd.DataFrame, column: str) -> bool:
    """
    Performs a Kolmogorov-Smirnov test to check if the distribution of a column is stable between two versions of the dataset.
    """
    # Drop missing values from the specified column
    data_v1 = dataset_v1[column].dropna()
    data_v2 = dataset_v2[column].dropna()

    # Print the number of non-null values for both datasets
    print(f"Non-null values for {column} in dataset_v1: {len(data_v1)}")
    print(f"Non-null values for {column} in dataset_v2: {len(data_v2)}")

    # Ensure that there are enough data points in both datasets
    if len(data_v1) < 10 or len(data_v2) < 10:
        print(f"Warning: Insufficient data for the column '{column}' to perform KS test.")
        return False

    # Ensure the columns have the same data type (convert to float64)
    data_v1 = data_v1.astype('float64')
    data_v2 = data_v2.astype('float64')

    # Perform the Kolmogorov-Smirnov test
    statistic, p_value = ks_2samp(data_v1, data_v2)
    
    # A p-value below 0.05 suggests the distributions are significantly different
    if p_value < 0.05:
        print(f"Statistical instability detected for column '{column}'. p-value: {p_value}")
        return False
    else:
        print(f"Column '{column}' is stable across versions. p-value: {p_value}")
        return True

if __name__ == "__main__":
    # Example dataset versions
    dataset_v1 = pd.read_csv('data/netflix_movies_detailed_up_to_2025.csv')  # Older dataset
    dataset_v2 = pd.read_csv('data/netflix_movies_cleaned.csv')  # Newer dataset

    # List of columns to test for stability
    columns_to_test = ['release_year', 'vote_average', 'popularity']  # You can add any columns you wish to compare

    # Test stability for each specified column
    for column in columns_to_test:
        print(f"\nTesting stability for column: {column}")
        if test_statistical_stability(dataset_v1, dataset_v2, column):
            print(f"The '{column}' column is stable over time.")
        else:
            print(f"The '{column}' column shows instability over time.")
