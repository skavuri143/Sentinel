import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'quality_rules')))

import pandas as pd
from quality_rules.missing_handle import handle_missing_values

def test_missing_values():
    datasets = {
        "Netflix Movies": 'data/netflix_movies_cleaned.csv',
        "Netflix TV Shows": 'data/netflix_tv_shows_cleaned.csv',
        "NYC Taxi Trip Data": 'data/nyc_taxi_trip_data_cleaned.csv'
    }
    
    for dataset_name, dataset_path in datasets.items():
        print(f"\nTesting missing values in {dataset_name} dataset...\n")
        
        # Load the dataset
        dataset = pd.read_csv(dataset_path)
        
        # Detect missing values before handling
        print(f"Missing values summary before handling for {dataset_name} dataset:")
        print(dataset.isnull().sum())
        
        # Handle missing values
        cleaned_dataset = handle_missing_values(dataset, dataset_name)
        
        # Check that no missing values remain after handling
        assert cleaned_dataset.isnull().sum().sum() == 0, f"Missing values not handled properly in {dataset_name}"
        
        print(f"Test passed: No missing values left in {dataset_name} dataset after handling.")
        
if __name__ == "__main__":
    test_missing_values()
