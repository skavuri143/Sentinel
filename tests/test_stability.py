import pandas as pd
from quality_rules.stability_tests import test_statistical_stability

def test_stability():
    dataset_paths = {
        "Netflix Movies": ['data/netflix_movies_v1.csv', 'data/netflix_movies_v2.csv'],
        "Netflix TV Shows": ['data/netflix_tv_shows_v1.csv', 'data/netflix_tv_shows_v2.csv'],
        "NYC Taxi Trip Data": ['data/nyc_taxi_trip_data_v1.csv', 'data/nyc_taxi_trip_data_v2.csv']
    }

    for dataset_name, dataset_paths in dataset_paths.items():
        print(f"\nTesting stability in {dataset_name} dataset...\n")
        
        # Load old and new dataset versions
        dataset_v1 = pd.read_csv(dataset_paths[0])
        dataset_v2 = pd.read_csv(dataset_paths[1])
        
        # Test stability for 'release_year' column
        result = test_statistical_stability(dataset_v1, dataset_v2, 'release_year')
        assert result, f"Statistical instability detected for {dataset_name} - 'release_year'"
        
        # Test stability for 'vote_average' column
        result = test_statistical_stability(dataset_v1, dataset_v2, 'vote_average')
        assert result, f"Statistical instability detected for {dataset_name} - 'vote_average'"
        
        # Test stability for 'popularity' column
        result = test_statistical_stability(dataset_v1, dataset_v2, 'popularity')
        assert result, f"Statistical instability detected for {dataset_name} - 'popularity'"

        print(f"Stability test passed for {dataset_name}.")
        
if __name__ == "__main__":
    test_stability()
