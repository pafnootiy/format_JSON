import json
import argparse
import os


def load_data(file_path="data.json"):
    with open(file_path, "r", encoding='utf-8', newline='') as file_obj:
        text = file_obj.read()
    data = json.loads(text)
    return data


def createParser():
    parser = argparse.ArgumentParser(description="formating .json files")
    parser.add_argument("data_file_path", type=str, nargs="?")

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    print(namespace)
    data = load_data(file_path=namespace.data_file_path)
    edit_data = json.dumps(data, sort_keys=True,
                           indent=4, ensure_ascii=False)
    print(edit_data)

