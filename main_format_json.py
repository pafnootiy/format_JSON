import json
import copy
from pprint import pprint


def load_flats(file_path=r"C:\users\alex K\desktop\python_projects\format_JSON\flats.json"):
    with open(file_path, "r",encoding='utf-8', newline='') as file_obj:
        text = file_obj.read()
    flats = json.loads(text)
    return flats

if __name__ == '__main__':  
    flats = load_flats()

    new_flat = copy.deepcopy(flats)
    edit_flat = json.dumps(new_flat,sort_keys=True, indent=4, ensure_ascii = False)


    print(edit_flat)

