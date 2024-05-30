import pandas as pd
import argparse


def basic_cleaning(input_file, output_file):
    data = pd.read_csv(input_file)

    data = data.dropna()
    data = data.drop_duplicates()

    X = data.drop('Species', axis=1)
    y = data['Species']

    preprocessed_data = pd.DataFrame(X, columns=X.columns)
    preprocessed_data['Species'] = y
    preprocessed_data.to_csv(output_file, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic data cleaning")
    parser.add_argument("input", help="Input CSV file")
    parser.add_argument("output", help="Output CSV file")
    args = parser.parse_args()

    basic_cleaning(args.input, args.output)
