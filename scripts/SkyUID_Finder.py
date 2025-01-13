import os

def find_uid_in_dump_files():
    base_directory = os.getcwd()
    print(f"Scanning directory and subdirectories from: \n{base_directory}\n")

    while True:
        try:
            user_input = input("Enter a 4-byte UID (or type 'exit' to quit): ").strip().upper()

            if user_input.lower() == "exit":
                break

            if len(user_input) != 8 or not all(c in "0123456789ABCDEF" for c in user_input):
                print("\nInvalid UID format. Example: D5A9CB0D\n")
                continue

            found_files = []

            for root, _, files in os.walk(base_directory):
                for filename in files:
                    if filename.endswith(".dump"):
                        filepath = os.path.join(root, filename)
                        relative_path = os.path.relpath(filepath, base_directory)

                        try:
                            with open(filepath, "rb") as file:
                                data = file.read(4)
                                hex_data = "".join(f"{byte:02X}" for byte in data)

                                if hex_data == user_input:
                                    found_files.append(relative_path)
                        except Exception as e:
                            print(f"Error reading file '{relative_path}': {e}")

            if found_files:
                print(f"\nThe UID {user_input} was found in the following file(s):")
                for file in found_files:
                    print(f"  {file}\n")
            else:
                print(f"\nThe UID {user_input} was not found in any dump files.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    try:
        find_uid_in_dump_files()
    except Exception as e:
        print(f"Fatal error: {e}")