import os
import json

# Get the current directory
current_directory = os.getcwd()

def has_date(operation: dict) -> bool:
    """
    To check if the operation has any appropriate date values.
    """
    if operation["ata"] or operation["atb"] or operation["atd"]:
        return True
    if operation["eta"] or operation["etb"] or operation["etd"]:
        return True
    if operation["cargo_discharged_date"]:
        return True
    if operation["cargo_loading_date"]:
        return True
    if operation["expected_cargo_loading_date"]:
        return True
    return False

# Function to check JSON files for the "ETA" field
def check_json_files_for_eta(directory):
    file_counter = 0
    # Loop through all files in the current directory
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_counter += 1
            file_path = os.path.join(directory, filename)
            print(f"Checking {filename}")
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                if isinstance(data, list):
                    for obj in data:
                        if has_date(obj):
                            pass
                            # print(f"Found date")
                        else:
                            print(f"ERROR: No date found in {obj['carrier']['name']}")
                print(f"Checked {len(data)} operations")

    print(f"Checked {file_counter} files")

# Call the function to check JSON files
check_json_files_for_eta(current_directory)
