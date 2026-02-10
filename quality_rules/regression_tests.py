import pandas as pd

def compare_datasets(dataset_v1: pd.DataFrame, dataset_v2: pd.DataFrame) -> bool:
    """
    Compare two versions of the dataset to ensure there are no regressions in the data.
    This is a simple comparison for missing values, schema, and key data columns.

    :param dataset_v1: The first version of the dataset (older version).
    :param dataset_v2: The second version of the dataset (newer version).
    :return: True if no regression is detected, False otherwise.
    """
    # Check schema consistency
    if not all(dataset_v1.columns == dataset_v2.columns):
        print("Schema mismatch detected between dataset versions.")
        return False

    # Check for missing values consistency
    missing_v1 = dataset_v1.isnull().sum()
    missing_v2 = dataset_v2.isnull().sum()
    
    print("Missing values in version 1:")
    print(missing_v1)
    print("\nMissing values in version 2:")
    print(missing_v2)

    if not missing_v1.equals(missing_v2):
        print("Missing value regression detected between dataset versions.")
        return False

    # Check for basic data consistency in key columns (e.g., 'show_id', 'rating')
    key_columns = ['show_id', 'title', 'rating', 'release_year']

    for column in key_columns:
        if column in dataset_v1.columns and column in dataset_v2.columns:
            if not dataset_v1[column].equals(dataset_v2[column]):
                print(f"Data regression detected in column: {column}")
                return False

    print("No regressions detected between dataset versions.")
    return True

if __name__ == "__main__":
    # Define the paths to the dataset versions
    datasets = {
        "Netflix Movies": ['data/netflix_movies_detailed_up_to_2025.csv', 'data/netflix_movies_cleaned.csv'],
        "Netflix TV Shows": ['data/netflix_tv_shows_detailed_up_to_2025.csv', 'data/netflix_tv_shows_cleaned.csv'],
        "NYC Taxi Trip Data": ['data/taxi_tripdata.csv', 'data/nyc_taxi_trip_data_cleaned.csv']
    }

    # Loop through each dataset pair and compare versions
    for dataset_name, dataset_paths in datasets.items():
        print(f"\nComparing {dataset_name} dataset...\n")
        
        try:
            # Load old (v1) and new (v2) dataset versions
            dataset_v1 = pd.read_csv(dataset_paths[0])
            dataset_v2 = pd.read_csv(dataset_paths[1])

            # Compare datasets
            if compare_datasets(dataset_v1, dataset_v2):
                print(f"Regression test passed for {dataset_name}.")
            else:
                print(f"Regression test failed for {dataset_name}.")
        
        except FileNotFoundError as e:
            print(f"Error: The file '{e.filename}' was not found. Please check the path.")
        except Exception as e:
            print(f"An error occurred while processing {dataset_name}: {e}")
