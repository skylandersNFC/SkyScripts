import os

def read_dump_file(file_path):
    try:
        with open(file_path, "rb") as file:
            binary_data = file.read()

        hex_data = binary_data.hex()
        return hex_data
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return None

def decode_skylanders_data(hex_data):
    try:
        data = bytes.fromhex(hex_data)

        if len(data) < 32:
            print("Error: Hex data is too short, expected at least 32 bytes.")
            return None, None

        # Extract CharacterID (bytes 0x10 to 0x11)
        character_id = int.from_bytes(data[0x10:0x12], byteorder="little")

        # Extract VariantID (bytes 0x1C and 0x1D)
        variant_id = int.from_bytes(data[0x1C:0x1E], byteorder="little")

        return character_id, variant_id
    except Exception as e:
        print(f"Error decoding data: {e}")
        return None, None

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    dump_files = []
    for root, _, files in os.walk(current_dir):
        for file in files:
            if file.endswith(".dump"):
                dump_files.append(os.path.join(root, file))

    if not dump_files:
        print("No .dump files found in the current directory or subdirectories.")
        return

    for dump_file in dump_files:
        file_name_without_extension = os.path.splitext(os.path.basename(dump_file))[0]
        hex_data = read_dump_file(dump_file)
        if not hex_data:
            print(f"Failed to read the file: {dump_file}")
            continue

        character_id, variant_id = decode_skylanders_data(hex_data)

        if character_id is not None and variant_id is not None:
            print(f"| {file_name_without_extension} | {character_id} | {variant_id} |")
        else:
            print(f"  Failed to decode data in file: {dump_file}")

if __name__ == "__main__":
    main()

input("\nPress Enter to exit...")
