import pandas as pd
from quality_rules.schema_validation import validate_schema

def test_schema():
    expected_schemas = {
        "Netflix Movies": {
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
        },
        "Netflix TV Shows": {
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
        },
        "NYC Taxi Trip Data": {
            'VendorID': 'Int64',
            'lpep_pickup_datetime': 'object',
            'lpep_dropoff_datetime': 'object',
            'store_and_fwd_flag': 'object',
            'RatecodeID': 'Int64',
            'PULocationID': 'Int64',
            'DOLocationID': 'Int64',
            'passenger_count': 'int64',
            'trip_distance': 'float64',
            'fare_amount': 'float64',
            'extra': 'float64',
            'mta_tax': 'float64',
            'tip_amount': 'float64',
            'tolls_amount': 'float64',
            'ehail_fee': 'float64',
            'improvement_surcharge': 'float64',
            'total_amount': 'float64',
            'payment_type': 'int64',
            'trip_type': 'int64',
            'congestion_surcharge': 'float64'
        }
    }

    for dataset_name, expected_schema in expected_schemas.items():
        print(f"\nTesting schema for {dataset_name} dataset...\n")
        
        # Load the dataset
        dataset = pd.read_csv(f"data/{dataset_name.lower().replace(' ', '_')}.csv")
        
        # Validate schema
        result = validate_schema(dataset, expected_schema)
        assert result, f"Schema validation failed for {dataset_name}"
        
        print(f"Schema validation passed for {dataset_name}.")
        
if __name__ == "__main__":
    test_schema()
