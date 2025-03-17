import os
import json

from DirectoryIterator import emulators_names
from MacroDebug import DEBUG

emulator_file_json_name = "EmulatorsPaths.json"



# 'r' to read, 'w' to write, 'a' to append, 'r+' to read/write

def create_json_file_emulator_data(current_directory):
    emulators_names_to_path = {}

    # init paths for the json file
    for i in range(len(emulators_names)):
        emulators_names_to_path[emulators_names[i]] = "C://"

    if DEBUG:
        print(emulators_names_to_path)

    file_name = os.path.join(current_directory, emulator_file_json_name)

    json_file = open(file_name, 'w')
    # write emulators to path into the file
    json_file.write(json.dumps(emulators_names_to_path, ensure_ascii=False, indent=4))
    json_file.close()

    if DEBUG:
        print("Emulator Files Registered to json file")


def read_file_emulator_test(current_directory):
    file_name = os.path.join(current_directory, emulator_file_json_name)
    json_file = open(file_name, 'r')
    data = json.load(json_file)
    print(data)
    print(data["3DS"])
    json_file.close()


def query_json_emulator_path(current_directory, emulator_name):
    # read from file and get the emulator path
    file_name = os.path.join(current_directory, emulator_file_json_name)
    json_file = open(file_name, 'r')
    # get data from file
    data = json.load(json_file)

    # query for the data
    if is_valid_json_index(data, emulator_name):
        json_file.close()
        file_path = data[emulator_name]
        return file_path
    else:
        json_file.close()
        return None


def is_valid_json_index(dict_data, emulator_name) -> bool:
    if emulator_name in dict_data:
        if DEBUG:
            print(True, "|Emulator Was Found In Json File")
        return True
    else:
        if DEBUG:
            print(False, "|Emulator Was Not Found In Json File")
        return False


def read_json_set_new_path(current_directory):
    file_name = os.path.join(current_directory, emulator_file_json_name)
    file_test = open(file_name, 'r+')
    data = json.load(file_test)
    if DEBUG:
        print(data)
        print(data["3DS"])
    data["3DS"] = "D://"
    # set file path to the beginning, so were not appending but rewriting
    file_test.seek(0)
    # write to file
    json.dump(data, file_test, indent=4)
    file_test.close()


create_json_file_emulator_data(os.getcwd())
read_json_set_new_path(os.getcwd())
query_json_emulator_path(os.getcwd(), "3DS")
query_json_emulator_path(os.getcwd(), "DS")
query_json_emulator_path(os.getcwd(), "NES")