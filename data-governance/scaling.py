import pandas as pd
from sklearn.preprocessing import StandardScaler
import argparse


def scaling(input_file, output_file):
    data = pd.read_csv(input_file)

    X = data.drop('Species', axis=1)
    y = data['Species']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    preprocessed_data = pd.DataFrame(X_scaled, columns=X.columns)
    preprocessed_data['Species'] = y
    preprocessed_data.to_csv(output_file, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data scaling")
    parser.add_argument("input", help="Input CSV file")
    parser.add_argument("output", help="Output CSV file")
    args = parser.parse_args()

    scaling(args.input, args.output)