import os

# Configurations for the Validation Engine

# Dataset paths
DATASETS_PATH = {
    "netflix_movies_v1": 'data/netflix_movies_detailed_up_to_2025.csv',
    "netflix_movies_v2": 'data/netflix_movies_cleaned.csv',
    "netflix_tv_shows_v1": 'data/netflix_tv_shows_detailed_up_to_2025.csv',
    "netflix_tv_shows_v2": 'data/netflix_tv_shows_cleaned.csv',
    "nyc_taxi_v1": 'data/taxi_tripdata.csv',
    "nyc_taxi_v2": 'data/nyc_taxi_trip_data_cleaned.csv'
}

# Columns to check for stability
COLUMNS_TO_CHECK = [
    "release_year",
    "vote_average",
    "popularity"
]

# Validation thresholds
MISSING_THRESHOLD = 0.35  # 35% missing values threshold to drop rows
STATISTICAL_TEST_ALPHA = 0.05  # p-value threshold for statistical tests

# Reporting configurations
REPORT_PATH = "reports/validation_report.txt"
LOG_PATH = "logs/validation_engine.log"
