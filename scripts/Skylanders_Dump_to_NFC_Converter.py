import os
import glob

def convert_dump_to_nfc(dump_file_path, output_nfc_path):
    header = [
        "Filetype: Flipper NFC device",
        "Version: 3",
        "Device type: Mifare Classic",
        "UID: {uid}",
        "ATQA: 00 04",
        "SAK: 08",
        "Mifare Classic type: 1K",
        "Data format version: 2"
    ]

    with open(dump_file_path, "rb") as f:
        data = f.read()

    if len(data) != 1024:
        print(f"Skipped {dump_file_path} (invalid size: {len(data)} bytes)")
        return

    uid = " ".join(f"{b:02X}" for b in data[0:4])
    header = [line.replace("{uid}", uid) for line in header]

    blocks = []
    for i in range(64):
        block = data[i*16:(i+1)*16]
        hex_str = " ".join(f"{b:02X}" for b in block)
        blocks.append(f"Block {i}: {hex_str}")

    with open(output_nfc_path, "w", encoding="utf-8") as out_file:
        for line in header + blocks:
            out_file.write(line + "\n")

    print(f"Converted: {os.path.basename(dump_file_path)} -> {os.path.basename(output_nfc_path)}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    dump_files = glob.glob("*.dump")
    if not dump_files:
        print("No .dump files found in the script directory.")
    else:
        for dump in dump_files:
            base_name = os.path.splitext(dump)[0]
            nfc_name = f"{base_name}.nfc"
            convert_dump_to_nfc(dump, nfc_name)

    input("\nDone! Press Enter to exit...")

if __name__ == "__main__":
    main()
