Sentinel
Sentinel is a comprehensive data validation and processing system designed for managing datasets. The project includes modules for handling missing values, schema validation, regression tests, and statistical stability checks for various datasets. It is aimed at ensuring high-quality, reliable data processing and analysis pipelines.
Features
•	Missing Value Handling: Detects and handles missing values across datasets.
•	Schema Validation: Ensures the data schema is consistent and meets expected formats.
•	Regression Testing: Compares different versions of datasets to detect regressions.
•	Statistical Stability Testing: Validates the consistency of data distributions between dataset versions.
Project Structure
Sentinel/
│
├── data/                       # Directory for datasets
│   ├── netflix_movies_v1.csv    # Original dataset for Netflix Movies
│   ├── netflix_movies_v2.csv    # Cleaned dataset for Netflix Movies
│   └── ...                     # Other datasets
│
├── quality_rules/              # Contains data validation scripts
│   ├── missing_handle.py       # Handles missing values in datasets
│   ├── schema_validation.py    # Validates dataset schemas
│   └── regression_tests.py     # Compares datasets for regressions
│
├── validation_engine/          # Directory for engine logic and configuration
│   ├── config.py               # Configuration file for validation engine
│   └── validate.py             # Main validation logic
│
├── tests/                      # Unit tests for validation rules
│   ├── test_missing_values.py  # Test missing values handling
│   ├── test_schema.py          # Test schema validation
│   └── test_regression.py      # Test regression functionality
│
└── validate_datasets.py        # Script for running validation on datasets
Installation
To get started with Sentinel, you will need Python and some dependencies installed. Follow these steps to set up the project:
Step 1: Clone the repository
Clone the repository to your local machine:
git clone https://github.com/your-username/Sentinel.git
cd Sentinel
Step 2: Install dependencies
It is recommended to use a virtual environment to manage dependencies. Create and activate a virtual environment:
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Then, install the necessary packages:
pip install -r requirements.txt
Step 3: Prepare datasets
Place your datasets in the data/ directory as described in the project structure.
Step 4: Run the validation
To run the validation scripts, use the following command:
python validate_datasets.py
This will initiate the dataset validation process, including schema validation, missing value handling, regression testing, and statistical stability checks.
Usage
•	Missing Values Handling: The project automatically detects missing values and can fill them with default values.
•	Schema Validation: It ensures that datasets comply with the expected column names and data types.
•	Regression Testing: It compares two versions of a dataset to detect any regressions in the data.
•	Statistical Stability: This feature tests if the data distribution remains stable between two versions of the dataset using statistical tests.
Tests
Unit tests are provided to ensure the correctness of the validation logic. You can run the tests using:
pytest tests/
Contributing
We welcome contributions! If you'd like to improve Sentinel, feel free to fork the repository, create a new branch, and submit a pull request. Please ensure that you write tests for any new functionality and that the existing tests pass.
License
This project is licensed under the MIT License.

