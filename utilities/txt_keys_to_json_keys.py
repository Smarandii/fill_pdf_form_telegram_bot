import json

def keys_to_json(input_file, output_file):
    with open(input_file, 'r') as in_file:
        keys = in_file.read().splitlines()
    # Create a dictionary where each key is associated with a numerical value
    keys_dict = {key: idx+1 for idx, key in enumerate(keys)}
    # Write the dictionary to a JSON file
    with open(output_file, 'w') as out_file:
        json.dump(keys_dict, out_file, indent=4)

# Call the function with your specific file paths
keys_to_json('input.txt', 'json_inputs/output.json')
