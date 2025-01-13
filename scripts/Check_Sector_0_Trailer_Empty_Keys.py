import os

def check_dump_files_for_zeros():
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith('.dump'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'rb') as f:
                        # Move to byte offset 0x30
                        f.seek(0x30)
                        # Read 6 bytes (0x30 to 0x35 inclusive)
                        data = f.read(6)

                        if data == b'\x00\x00\x00\x00\x00\x00':
                            print(f"Empty 0x00 value Keys found: {file_path}")
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

if __name__ == "__main__":
    check_dump_files_for_zeros()
    
input("\nPress Enter to exit...")