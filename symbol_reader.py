#where the map map symbol dictionary will be read.
import yaml

def load_dictionary_yaml(filename):
    with open(filename) as f:
        data = yaml.safe_load(f)
    return data
