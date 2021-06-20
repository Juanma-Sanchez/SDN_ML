import yaml

def load(filename: str) -> dict:
    with open(filename, 'r') as f:
        return yaml.load(f)

def dump(dictionary: dict, filename: str):
    with open(filename, 'w') as f:
        yaml.dump(dictionary, f)
