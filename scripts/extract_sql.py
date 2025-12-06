import pandas as pd
import sqlalchemy as sa

def load_sql():
    engine = sa.create_engine("mysql+pymysql://user:pass@localhost/db_name")
    df = pd.read_sql("SELECT * FROM my_table", engine)
    print(df.head())
    return df

if __name__ == "__main__":
    load_sql()
