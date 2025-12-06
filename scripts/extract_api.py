import requests

def load_api():
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    data = r.json()
    print("API Data:", data[:3])
    return data

if __name__ == "__main__":
    load_api()
