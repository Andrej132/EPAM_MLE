"""
This module performs basic data cleaning operations on a CSV file.
"""

import argparse
import pandas as pd


def basic_cleaning(input_file, output_file):
    """
    Perform basic data cleaning operations on the input CSV file.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
    """
    data = pd.read_csv(input_file)

    data = data.dropna()
    data = data.drop_duplicates()

    features = data.drop('Species', axis=1)
    target = data['Species']

    preprocessed_data = pd.DataFrame(features, columns=features.columns)
    preprocessed_data['Species'] = target
    preprocessed_data.to_csv(output_file, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic data cleaning")
    parser.add_argument("input", help="Input CSV file")
    parser.add_argument("output", help="Output CSV file")
    args = parser.parse_args()

    basic_cleaning(args.input, args.output)
