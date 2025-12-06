import boto3

def load_from_s3():
    s3 = boto3.client("s3")
    s3.download_file("my-bucket", "data.csv", "data/csv/from_s3.csv")
    print("File Downloaded from S3")
    return True

if __name__ == "__main__":
    load_from_s3()
