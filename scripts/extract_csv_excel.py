import pandas as pd

def load_csv(path="data/csv/sample.csv"):
    df = pd.read_csv(path)
    print("CSV Loaded:")
    print(df.head())
    return df

def load_excel(path="data/excel/sample.xlsx"):
    df = pd.read_excel(path)
    print("Excel Loaded:")
    print(df.head())
    return df

if __name__ == "__main__":
    load_csv()
    load_excel()
