import os
from collections import defaultdict

def find_duplicate_hex_in_dump_files(base_directory):
    hex_dict = defaultdict(list)
    print(f"Scanning directory and subdirectories from: {base_directory}\n")

    for root, _, files in os.walk(base_directory):
        for filename in files:
            if filename.endswith(".dump"):
                filepath = os.path.join(root, filename)
                relative_path = os.path.relpath(filepath, base_directory)

                try:
                    with open(filepath, "rb") as file:
                        data = file.read(4)
                        hex_data = " ".join(f"{byte:02X}" for byte in data)
                        hex_dict[hex_data].append(relative_path)
                except Exception as e:
                    print(f"Error reading file '{relative_path}': {e}")

    duplicates = {hex_val: files for hex_val, files in hex_dict.items() if len(files) > 1}

    if duplicates:
        print("Duplicate 4-byte HEX sequences found:\n")
        for hex_val, files in duplicates.items():
            print(f"HEX: {hex_val} - Found in files:")
            for file in files:
                print(f"  {file}")
    else:
        print("No duplicate 4-byte HEX sequences found.")

current_directory = os.getcwd()
find_duplicate_hex_in_dump_files(current_directory)
input("Press Enter to exit...")