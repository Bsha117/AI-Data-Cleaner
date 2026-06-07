import json
import struct
import sys

def convert_dat_to_json(input_file, output_file):
    data = []
    try:
        with open(input_file, 'rb') as f:
            while True:
                chunk = f.read(4)
                if not chunk:
                    break
                val = struct.unpack('f', chunk)[0]
                data.append({"value": val})
        
        with open(output_file, 'w') as f:
            json.dump({"status": "success", "data": data}, f, indent=4)
        print(f"Conversion successful. Data saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        convert_dat_to_json(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python dat_to_json.py <input_file.dat> <output_file.json>")
