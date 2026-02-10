import pandas as pd

def detect_missing_values(dataset: pd.DataFrame) -> pd.DataFrame:
    """
    Detect missing values in the dataset and return a summary report.

    :param dataset: DataFrame representing the dataset.
    :return: DataFrame containing the count and percentage of missing values per column.
    """
    # Calculate the number of missing values for each column
    missing_data = dataset.isnull().sum()
    
    # Calculate the percentage of missing values for each column
    missing_percentage = (missing_data / len(dataset)) * 100
    
    # Create a summary DataFrame containing missing count and percentage
    missing_summary = pd.DataFrame({'missing_count': missing_data, 'missing_percentage': missing_percentage})
    
    # Return the summary
    return missing_summary

if __name__ == "__main__":
    # Define the paths to the datasets
    datasets = {
        "Netflix Movies": 'data/netflix_movies_detailed_up_to_2025.csv',
        "Netflix TV Shows": 'data/netflix_tv_shows_detailed_up_to_2025.csv',
        "NYC Taxi Trip Data": 'data/taxi_tripdata.csv',
        "Netflix Movies Cleaned": 'data/netflix_movies_cleaned.csv',
        "Netflix TV Shows Cleaned": 'data/netflix_tv_shows_cleaned.csv',
        "NYC Taxi Trip Data Cleaned": 'data/nyc_taxi_trip_data_cleaned.csv'
    }

    # Loop through each dataset and detect missing values
    for dataset_name, dataset_path in datasets.items():
        print(f"\nDetecting missing values in {dataset_name} dataset...\n")
        
        try:
            # Load the dataset
            dataset = pd.read_csv(dataset_path)
            
            # Detect missing values and get the summary
            missing_summary = detect_missing_values(dataset)
            
            # Print the summary of missing values
            print(f"Missing values summary for {dataset_name} dataset:")
            print(missing_summary)
        except FileNotFoundError:
            print(f"Error: The file '{dataset_path}' was not found. Please check the path.")
        except Exception as e:
            print(f"An error occurred while processing {dataset_name}: {e}")
