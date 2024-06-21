"""
This module performs outlier detection on a CSV file using z-scores.
"""

import argparse
import pandas as pd
import numpy as np


def outlier_detection(input_file, output_file):
    """
    Detect and remove outliers in the input CSV file.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
    """
    df = pd.read_csv(input_file)

    features = df.drop('Species', axis=1)

    z_scores = (features - features.mean()) / features.std()
    outliers = (np.abs(z_scores) > 3).any(axis=1)

    preprocessed_df = df[~outliers]
    preprocessed_df.to_csv(output_file, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Outlier detection")
    parser.add_argument("input", help="Input CSV file")
    parser.add_argument("output", help="Output CSV file")
    args = parser.parse_args()

    outlier_detection(args.input, args.output)
