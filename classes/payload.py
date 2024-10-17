import json

def load_data():
    file_path = "data/data.json"
    try:
        with open(file_path, "r", encoding="utf-8") as data_file:
            data = json.load(data_file)
        return data
    except FileNotFoundError:
        with open(file_path, "w") as data_file:
            data = json.dump({"tasks": []}, data_file)
            
        
def load_config():
    file_path = "config.json"
    try:
        with open(file_path, "r") as config_file:
            config = json.load(config_file)
            return config
    except FileNotFoundError:
        with open(file_path,"w") as config_file:
            config = {"theme":"Light", "language":"Polish"}
            json.dump(config, config_file)
            return config