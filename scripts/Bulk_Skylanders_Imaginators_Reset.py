import os
import logging

SECTOR_SIZE = 64
BLOCK_SIZE = 16

PRESERVED_BLOCKS = {
    (1, 0),   # Sector 1, Block 0
    (8, 2),   # Sector 8, Block 2
    (15, 2)   # Sector 15, Block 2
}

logging.basicConfig(level=logging.INFO, format='%(message)s')

def read_nfc_dump(file_path):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        sectors = [data[i:i + SECTOR_SIZE] for i in range(0, len(data), SECTOR_SIZE)]
        return sectors
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")
        return None

def write_nfc_dump(file_path, sectors):
    try:
        with open(file_path, 'wb') as f:
            for sector in sectors:
                f.write(sector)
    except Exception as e:
        logging.error(f"Error writing to file {file_path}: {e}")

def zero_non_preserved_blocks(sectors):
    for sector_index, sector in enumerate(sectors):
        if sector_index == 0:
            continue
        
        blocks = [sector[i:i + BLOCK_SIZE] for i in range(0, len(sector), BLOCK_SIZE)]
        
        for block_index in range(3):
            if (sector_index, block_index) not in PRESERVED_BLOCKS:                      
                blocks[block_index] = bytes(BLOCK_SIZE)
        
        sectors[sector_index] = b''.join(blocks)
    return sectors

def process_nfc_dumps_in_folder(folder_name):
    for root, dirs, files in os.walk(folder_name):
        for filename in files:
            if filename.endswith('.dump'):
                full_path = os.path.join(root, filename)
                sectors = read_nfc_dump(full_path)
                if sectors is not None:
                    sectors = zero_non_preserved_blocks(sectors)
                    write_nfc_dump(full_path, sectors)
                    logging.info(f"Resetting Skylander dump: {full_path}")

process_nfc_dumps_in_folder('.')
for folder_name in os.listdir('.'):
    if os.path.isdir(folder_name):
        process_nfc_dumps_in_folder(folder_name)

input("Press Enter to exit...")