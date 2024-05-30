import pandas as pd
import numpy as np
import argparse


def outlier_detection(input_file, output_file):
    df = pd.read_csv(input_file)

    X = df.drop('Species', axis=1)
    y = df['Species']

    z_scores = (X - X.mean()) / X.std()
    outliers = (np.abs(z_scores) > 3).any(axis=1)

    preprocessed_df = df[~outliers]
    preprocessed_df.to_csv(output_file, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Outlier detection")
    parser.add_argument("input", help="Input CSV file")
    parser.add_argument("output", help="Output CSV file")
    args = parser.parse_args()

    outlier_detection(args.input, args.output)
