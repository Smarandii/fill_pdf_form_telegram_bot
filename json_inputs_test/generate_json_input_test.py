import json

# Reading the newly uploaded JSON file
with open("i-131-test-data.json", "r", encoding="utf-8-sig") as file:
    i_485_data = json.load(file)


def fill_with_ascending_numbers(data):
    counter = 1
    for key in data.keys():
        data[key] = str(counter)
        counter += 1
    return data


# Filling the JSON structure with ascending numbers starting from 1
counter_i_485 = fill_with_ascending_numbers(i_485_data)

# Saving the modified JSON structure back to a file
modified_i_485_filepath = "i-131-test-data.json"
with open(modified_i_485_filepath, "w") as file:
    json.dump(i_485_data, file, indent=4)

