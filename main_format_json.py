import json


def load_data(file_path=r"data.json"):
    with open(file_path, "r", encoding='utf-8', newline='') as file_obj:
        text = file_obj.read()
    data = json.loads(text)
    return data


if __name__ == '__main__':

    data = load_data()
    edit_data = json.dumps(data, sort_keys=True,
                           indent=4, ensure_ascii=False)

    print(edit_data)
