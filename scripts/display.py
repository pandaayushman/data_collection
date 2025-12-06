import pandas as pd

def display_sample(df):
    print("Displaying data:")
    print(df.head())

if __name__ == "__main__":
    df = pd.DataFrame({"A":[1,2,3]})
    display_sample(df)
