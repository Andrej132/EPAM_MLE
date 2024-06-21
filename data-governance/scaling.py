"""
This module performs scaling of features in a CSV file using StandardScaler.
"""

import argparse
import pandas as pd
from sklearn.preprocessing import StandardScaler


def scaling(input_file, output_file):
    """
    Scale features in the input CSV file and save the scaled data to the output CSV file.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
    """
    data = pd.read_csv(input_file)

    features = data.drop('Species', axis=1)
    target = data['Species']

    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    preprocessed_data = pd.DataFrame(features_scaled, columns=features.columns)
    preprocessed_data['Species'] = target
    preprocessed_data.to_csv(output_file, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data scaling")
    parser.add_argument("input", help="Input CSV file")
    parser.add_argument("output", help="Output CSV file")
    args = parser.parse_args()

    scaling(args.input, args.output)
