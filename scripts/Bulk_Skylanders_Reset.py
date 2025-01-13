import os

def read_nfc_dump(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    sectors = [data[i:i + 64] for i in range(0, len(data), 64)]
    return sectors

def write_nfc_dump(file_path, sectors):
    with open(file_path, 'wb') as f:
        for sector in sectors:
            f.write(sector)

def zero_non_preserved_blocks(sectors):
    for sector_index, sector in enumerate(sectors):
        if sector_index == 0:
            continue
        
        blocks = [sector[i:i + 16] for i in range(0, len(sector), 16)]
        for block_index in range(4):
            if block_index != 3:
                blocks[block_index] = bytes(16)
        sectors[sector_index] = b''.join(blocks)
    return sectors

def process_dump_files(folder_name):
    for root, dirs, files in os.walk(folder_name):
        for filename in files:
            if filename.endswith('.dump'):
                full_path = os.path.join(root, filename)
                sectors = read_nfc_dump(full_path)
                sectors = zero_non_preserved_blocks(sectors)
                write_nfc_dump(full_path, sectors)
                print(f"Resetting Skylander: {full_path}")

process_dump_files('.')

for folder_name in os.listdir('.'):
    if os.path.isdir(folder_name):
        process_dump_files(folder_name)

input("Press Enter to exit...")