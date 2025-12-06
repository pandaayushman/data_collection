import pandas as pd

def trim_data():
    df = pd.DataFrame({"name": [" Alice ", " Bob  ", "  Carol"]})
    df["name"] = df["name"].str.strip()
    print(df)
    return df

if __name__ == "__main__":
    trim_data()
