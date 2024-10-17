import json

def save_data(data):
    file_path = "data/data.json"
    try:
        with open(file_path, 'w', encoding="utf-8") as data_file:
            json.dump(data, data_file, ensure_ascii=False)
    except Exception as e:
        print(f"Error:{e}")

def save_config(config):
    file_path = "config.json"
    try:
        with open(file_path, 'w', encoding="utf-8") as config_file:
            json.dump(config, config_file, ensure_ascii=False)
    except Exception as e:
        print(f"ErrorL: {e}")