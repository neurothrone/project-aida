import json


def load_data_from_json(path: str) -> dict:
    with open(path, "r") as file_in:
        return json.load(file_in)


def save_data_to_json(path: str) -> None:
    pass
