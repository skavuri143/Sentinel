import pandas as pd
from quality_rules.regression_tests import compare_datasets

def test_regression():
    dataset_paths = {
        "Netflix Movies": ['data/netflix_movies_v1.csv', 'data/netflix_movies_v2.csv'],
        "Netflix TV Shows": ['data/netflix_tv_shows_v1.csv', 'data/netflix_tv_shows_v2.csv'],
        "NYC Taxi Trip Data": ['data/nyc_taxi_trip_data_v1.csv', 'data/nyc_taxi_trip_data_v2.csv']
    }

    for dataset_name, dataset_paths in dataset_paths.items():
        print(f"\nTesting regression in {dataset_name} dataset...\n")
        
        # Load old and new dataset versions
        dataset_v1 = pd.read_csv(dataset_paths[0])
        dataset_v2 = pd.read_csv(dataset_paths[1])
        
        # Compare the datasets for regressions
        result = compare_datasets(dataset_v1, dataset_v2)
        assert result, f"Regression test failed for {dataset_name}"
        
        print(f"Regression test passed for {dataset_name}.")
        
if __name__ == "__main__":
    test_regression()
