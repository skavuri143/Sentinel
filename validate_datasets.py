import pandas as pd
import logging
from scipy.stats import ks_2samp

# Function to handle missing values detection
def detect_missing_values(dataset: pd.DataFrame):
    missing_data = dataset.isnull().sum()
    missing_percentage = (missing_data / len(dataset)) * 100
    return pd.DataFrame({'missing_count': missing_data, 'missing_percentage': missing_percentage})

# Function for regression test comparison
def compare_datasets(dataset_v1: pd.DataFrame, dataset_v2: pd.DataFrame):
    # Compare schema, missing values, and perform statistical tests
    print("Comparing datasets...")

    # Example of handling missing 'release_year' column
    columns_to_check = ['release_year', 'vote_average', 'popularity']
    for column in columns_to_check:
        if column in dataset_v1.columns and column in dataset_v2.columns:
            print(f"Testing stability for column: {column}")
            # Perform the statistical test or missing value comparison
            ks_test(dataset_v1, dataset_v2, column)
        else:
            print(f"Warning: Column '{column}' is missing in one of the datasets.")

# Function to perform KS test
def ks_test(dataset_v1: pd.DataFrame, dataset_v2: pd.DataFrame, column: str):
    # Drop missing values
    data_v1 = dataset_v1[column].dropna()
    data_v2 = dataset_v2[column].dropna()

    # Perform the Kolmogorov-Smirnov test
    statistic, p_value = ks_2samp(data_v1, data_v2)
    
    # A p-value below 0.05 suggests the distributions are significantly different
    if p_value < 0.05:
        print(f"Statistical instability detected for column '{column}'. p-value: {p_value}")
    else:
        print(f"Column '{column}' is stable across versions. p-value: {p_value}")

# Function to validate schema
def validate_schema(dataset: pd.DataFrame, expected_schema: dict):
    # Check schema consistency
    print(f"Validating schema for dataset...")
    for column, expected_dtype in expected_schema.items():
        if column not in dataset.columns:
            print(f"Error: Missing column '{column}'")
            return False
        if not pd.api.types.is_dtype_equal(dataset[column].dtype, expected_dtype):
            print(f"Error: Column '{column}' has incorrect type. Expected {expected_dtype}, found {dataset[column].dtype}")
            return False
    return True

# Main validation script
def main():
    # Dataset paths as provided
    DATASETS_PATH = {
        "netflix_movies_v1": 'data/netflix_movies_detailed_up_to_2025.csv',
        "netflix_movies_v2": 'data/netflix_movies_cleaned.csv',
        "netflix_tv_shows_v1": 'data/netflix_tv_shows_detailed_up_to_2025.csv',
        "netflix_tv_shows_v2": 'data/netflix_tv_shows_cleaned.csv',
        "nyc_taxi_v1": 'data/taxi_tripdata.csv',
        "nyc_taxi_v2": 'data/nyc_taxi_trip_data_cleaned.csv'
    }
    
    # Example schema for Netflix Movies
    netflix_movies_schema = {
        'show_id': 'object',
        'type': 'object',
        'title': 'object',
        'director': 'object',
        'cast': 'object',
        'country': 'object',
        'date_added': 'object',
        'release_year': 'int64',
        'rating': 'object',
        'duration': 'object',
        'genres': 'object',
        'language': 'object',
        'description': 'object',
        'popularity': 'float64',
        'vote_count': 'int64',
        'vote_average': 'float64',
        'budget': 'int64',
        'revenue': 'int64'
    }

    # Load and validate each dataset
    for dataset_name, dataset_path in DATASETS_PATH.items():
        try:
            dataset = pd.read_csv(dataset_path)
            print(f"Dataset loaded: {dataset_name}")
            
            # Validate schema for the dataset
            if validate_schema(dataset, netflix_movies_schema):
                print(f"Schema validation passed for {dataset_name}.\n")
            else:
                print(f"Schema validation failed for {dataset_name}.\n")

            # Check for missing values
            print(f"Missing values in {dataset_name}:")
            print(detect_missing_values(dataset))

            # Compare dataset versions (regression test)
            if "v1" in dataset_name and "v2" in DATASETS_PATH:
                compare_datasets(pd.read_csv(DATASETS_PATH[dataset_name.replace("v1", "v2")]), dataset)

        except FileNotFoundError:
            print(f"Error: {dataset_path} not found.")
        except Exception as e:
            print(f"An error occurred while processing {dataset_name}: {e}")

if __name__ == '__main__':
    main()
