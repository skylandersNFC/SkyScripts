import os
import glob

def modify_dump_file(file_path):
    try:
        with open(file_path, 'r+b') as file:
            file.seek(54)
            file.write(bytes([0xFF, 0x07, 0x80]))
        
        print(f"File '{file_path}' modified successfully.")
    except Exception as e:
        print(f"An error occurred while modifying '{file_path}': {e}")

def modify_all_dump_files_in_directory():
    main_directory = os.getcwd()
    for file_path in glob.glob(os.path.join(main_directory, '**', '*.dump'), recursive=True):
        modify_dump_file(file_path)
        
modify_all_dump_files_in_directory()

input("Press Enter to exit...")