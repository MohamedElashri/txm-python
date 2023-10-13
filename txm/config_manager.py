import json

def load_config(file_path=".txm-config.json"):
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        return {}
