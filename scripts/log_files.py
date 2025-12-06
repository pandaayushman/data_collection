import json

def load_log(path="data/logs/system.log"):
    with open(path) as f:
        logs = f.readlines()
    print("Logs:", logs[:3])
    return logs

def load_json(path="data/json/sample.json"):
    with open(path) as f:
        data = json.load(f)
    print("JSON Data:", data)
    return data

if __name__ == "__main__":
    load_log()
    load_json()
