import pandas as pd

def validate_schema(dataset: pd.DataFrame, expected_schema: dict) -> bool:
    """
    Validates the schema of the given dataset by comparing the columns and their data types to the expected schema.

    :param dataset: DataFrame representing the dataset.
    :param expected_schema: Dictionary with column names as keys and expected data types as values.
    :return: True if schema is valid, False otherwise.
    """
    for column, expected_dtype in expected_schema.items():
        if column not in dataset.columns:
            print(f"Error: Missing column '{column}'")
            return False
        if not pd.api.types.is_dtype_equal(dataset[column].dtype, expected_dtype):
            print(f"Error: Column '{column}' has incorrect type. Expected {expected_dtype}, found {dataset[column].dtype}")
            return False
    return True

if __name__ == "__main__":
    # Expected schema for Netflix movies dataset
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

    # Expected schema for Netflix TV shows dataset
    netflix_tv_shows_schema = {
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
        'vote_average': 'float64'
    }

    # Expected schema for NYC Taxi trips dataset
    taxi_tripdata_schema = {
        'VendorID': 'Int64',  # Use 'Int64' to handle nullable integer type
        'lpep_pickup_datetime': 'object',
        'lpep_dropoff_datetime': 'object',
        'store_and_fwd_flag': 'object',
        'RatecodeID': 'Int64',  # Use 'Int64' for nullable integers, which handles NA values
        'PULocationID': 'Int64',  # Use 'Int64' for nullable integers
        'DOLocationID': 'Int64',  # Use 'Int64' for nullable integers
        'passenger_count': 'Int64',  # Change to 'Int64' to handle missing values
        'trip_distance': 'float64',
        'fare_amount': 'float64',
        'extra': 'float64',
        'mta_tax': 'float64',
        'tip_amount': 'float64',
        'tolls_amount': 'float64',
        'improvement_surcharge': 'float64',
        'total_amount': 'float64',
        'payment_type': 'float64',  # Use 'Int64' for nullable integers
        'trip_type': 'float64',  # Use 'Int64' for nullable integers
        'congestion_surcharge': 'float64'
    }

    # Load and validate Netflix movies dataset with proper types
    try:
        netflix_movies = pd.read_csv(
            'data/netflix_movies_detailed_up_to_2025.csv', 
            dtype={'show_id': 'object', 'rating': 'object', 'duration': 'object'},  # Ensure 'rating' and 'duration' are treated as 'object'
            na_values={'rating': 'Unknown', 'duration': 'Unknown'}  # Handle missing values in 'rating' and 'duration' by filling with 'Unknown'
        )
        if validate_schema(netflix_movies, netflix_movies_schema):
            print("Schema validation passed for Netflix movies dataset!")
        else:
            print("Schema validation failed for Netflix movies dataset.")
    except Exception as e:
        print(f"Error loading Netflix movies dataset: {e}")

    # Load and validate Netflix TV shows dataset with proper types
    try:
        netflix_tv_shows = pd.read_csv(
            'data/netflix_tv_shows_detailed_up_to_2025.csv', 
            dtype={'show_id': 'object', 'rating': 'object', 'duration': 'object'},  # Ensure 'rating' and 'duration' are treated as 'object'
            na_values={'rating': 'Unknown', 'duration': 'Unknown'}  # Handle missing values in 'rating' and 'duration' by filling with 'Unknown'
        )
        if validate_schema(netflix_tv_shows, netflix_tv_shows_schema):
            print("Schema validation passed for Netflix TV shows dataset!")
        else:
            print("Schema validation failed for Netflix TV shows dataset.")
    except Exception as e:
        print(f"Error loading Netflix TV shows dataset: {e}")

    # Load and validate NYC Taxi trips dataset with proper types
    try:
        taxi_tripdata = pd.read_csv(
            'data/taxi_tripdata.csv', 
            dtype={
                'VendorID': 'Int64', 'RatecodeID': 'Int64', 'PULocationID': 'Int64', 'DOLocationID': 'Int64', 
                'passenger_count': 'Int64'  # Handle nullable integers
            },  
            na_values={
                'VendorID': -1, 'RatecodeID': -1, 'PULocationID': -1, 'DOLocationID': -1, 'passenger_count': 0  # Handle missing values
            }  
        )
        if validate_schema(taxi_tripdata, taxi_tripdata_schema):
            print("Schema validation passed for NYC Taxi trips dataset!")
        else:
            print("Schema validation failed for NYC Taxi trips dataset.")
    except Exception as e:
        print(f"Error loading NYC Taxi trips dataset: {e}")
