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

def handle_missing_values(dataset: pd.DataFrame, dataset_name: str) -> pd.DataFrame:
    """
    This function handles missing values in the dataset by:
    - Filling or removing values based on the dataset.
    - Dropping rows that contain missing values.
    
    :param dataset: DataFrame representing the dataset.
    :param dataset_name: Name of the dataset (e.g., "Netflix Movies", "NYC Taxi").
    :return: Cleaned DataFrame with missing values handled.
    """
    # Remove rows with any missing values (this will drop rows with NaN in any column)
    dataset = dataset.dropna(how='any')  # 'how' can be 'any' or 'all'

    # Drop 'ehail_fee' column since it has 100% missing values
    if 'ehail_fee' in dataset.columns:
        dataset = dataset.drop(columns=['ehail_fee'])

    # Handle missing values for Netflix Movies and TV Shows datasets
    if dataset_name == "Netflix Movies" or dataset_name == "Netflix TV Shows":
        if 'duration' in dataset.columns:
            dataset['duration'] = dataset['duration'].fillna('Unknown')  # Impute missing duration with 'Unknown'
        if 'director' in dataset.columns:
            dataset['director'] = dataset['director'].fillna('Unknown')  # Impute missing director with 'Unknown'
        if 'cast' in dataset.columns:
            dataset['cast'] = dataset['cast'].fillna('Unknown')  # Impute missing cast with 'Unknown'
        if 'country' in dataset.columns:
            dataset['country'] = dataset['country'].fillna('Unknown')  # Impute missing country with 'Unknown'
        if 'description' in dataset.columns:
            dataset['description'] = dataset['description'].fillna('Unknown')  # Impute missing description with 'Unknown'
        if 'genres' in dataset.columns:
            dataset['genres'] = dataset['genres'].fillna('Unknown')  # Impute missing genres with 'Unknown'

    # Handle missing values for NYC Taxi dataset
    if dataset_name == "NYC Taxi":
        if 'VendorID' in dataset.columns:
            dataset['VendorID'] = dataset['VendorID'].fillna(-1).astype('Int64')  # Fill missing VendorID with -1 (nullable int)
        if 'RatecodeID' in dataset.columns:
            dataset['RatecodeID'] = dataset['RatecodeID'].fillna(-1).astype('Int64')  # Fill missing RatecodeID with -1 (nullable int)
        if 'PULocationID' in dataset.columns:
            dataset['PULocationID'] = dataset['PULocationID'].fillna(-1).astype('Int64')  # Fill missing PULocationID with -1 (nullable int)
        if 'DOLocationID' in dataset.columns:
            dataset['DOLocationID'] = dataset['DOLocationID'].fillna(-1).astype('Int64')  # Fill missing DOLocationID with -1 (nullable int)
        if 'passenger_count' in dataset.columns:
            dataset['passenger_count'] = dataset['passenger_count'].fillna(0).astype('int64')  # Fill missing passenger_count with 0
        if 'store_and_fwd_flag' in dataset.columns:
            dataset['store_and_fwd_flag'] = dataset['store_and_fwd_flag'].fillna('Unknown')  # Fill missing flag with 'Unknown'
        if 'congestion_surcharge' in dataset.columns:
            dataset['congestion_surcharge'] = dataset['congestion_surcharge'].fillna(0)  # Fill missing congestion_surcharge with 0

    return dataset

if __name__ == "__main__":
    # Define the paths to the datasets
    datasets = {
        "Netflix Movies": 'data/netflix_movies_detailed_up_to_2025.csv',
        "Netflix TV Shows": 'data/netflix_tv_shows_detailed_up_to_2025.csv',
        "NYC Taxi Trip Data": 'data/taxi_tripdata.csv'
    }

    # Loop through each dataset and handle missing values
    for dataset_name, dataset_path in datasets.items():
        print(f"\nHandling missing values in {dataset_name} dataset...\n")
        
        try:
            # Load the dataset
            dataset = pd.read_csv(dataset_path)
            
            # Detect and print missing values before handling
            print(f"Missing values summary before handling for {dataset_name} dataset:")
            print(detect_missing_values(dataset))
            
            # Handle missing values
            cleaned_dataset = handle_missing_values(dataset, dataset_name)
            
            # Save cleaned data (optional, if you want to save it for later use)
            cleaned_dataset.to_csv(f'data/{dataset_name.replace(" ", "_").lower()}_cleaned.csv', index=False)

            # Print summary after handling missing values
            print(f"Missing values summary after handling for {dataset_name} dataset:")
            print(detect_missing_values(cleaned_dataset))

            print(f"Missing values handled and cleaned data saved for {dataset_name}.")
        except FileNotFoundError:
            print(f"Error: The file '{dataset_path}' was not found. Please check the path.")
        except Exception as e:
            print(f"An error occurred while processing {dataset_name}: {e}")
