import sys
sys.path.append('d:/Download-Office/ITF-JW-GTC-SK-04/Sentinel')

import pandas as pd
import logging
from config import DATASETS_PATH, COLUMNS_TO_CHECK, MISSING_THRESHOLD, REPORT_PATH, STATISTICAL_TEST_ALPHA
from quality_rules.schema_validation import validate_schema
from quality_rules.missing_handle import handle_missing_values
from quality_rules.regression_tests import compare_datasets
from quality_rules.stability_tests import test_statistical_stability

# Setup logging
logging.basicConfig(filename="logs/validation_engine.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def generate_report():
    with open(REPORT_PATH, 'w') as report_file:
        report_file.write("Validation Report\n")
        report_file.write("====================\n")

        # Iterate through each dataset and run the validation functions
        for dataset_name, dataset_path in DATASETS_PATH.items():
            try:
                logging.info(f"Validating {dataset_name}...")

                # Load the dataset
                dataset = pd.read_csv(dataset_path)

                # Handle missing values
                cleaned_dataset = handle_missing_values(dataset, dataset_name)
                missing_values = cleaned_dataset.isnull().sum()

                report_file.write(f"\nDataset: {dataset_name}\n")
                report_file.write(f"Missing values summary: {missing_values}\n")

                # Perform schema validation
                expected_schema = {}  # Define expected schema based on your dataset
                if validate_schema(cleaned_dataset, expected_schema):
                    report_file.write("Schema validation: PASSED\n")
                else:
                    report_file.write("Schema validation: FAILED\n")

                # Perform regression tests with previous dataset versions
                dataset_v1 = pd.read_csv(DATASETS_PATH[dataset_name.replace("v2", "v1")])
                if compare_datasets(dataset_v1, cleaned_dataset):
                    report_file.write("Regression test: PASSED\n")
                else:
                    report_file.write("Regression test: FAILED\n")

                # Perform statistical stability tests
                for column in COLUMNS_TO_CHECK:
                    if test_statistical_stability(dataset_v1, cleaned_dataset, column):
                        report_file.write(f"Statistical stability for column {column}: PASSED\n")
                    else:
                        report_file.write(f"Statistical stability for column {column}: FAILED\n")

                logging.info(f"Validation for {dataset_name} completed.")
            except Exception as e:
                logging.error(f"Error processing {dataset_name}: {e}")
                report_file.write(f"\nError processing {dataset_name}: {e}\n")

    logging.info("Report generation completed.")

if __name__ == "__main__":
    generate_report()
