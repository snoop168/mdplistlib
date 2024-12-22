from mdplist import load
import argparse
import os
import json

def main():
    # Parse the arguments
    parser = argparse.ArgumentParser(description="Convert an mdplist file to json")
    parser.add_argument("filename", help="Path to the file to process")
    args = parser.parse_args()

    # Get the input file path and namen
    input_file = args.filename

    # Ensure the input file exists
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        return

    try:
        output_data = load(input_file)
    except Exception as e:
        print(f"Error processing file: {e}")
        return

    # Define the output file name in the same directory with _processed
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}.json"

    # Write the output data to the file
    try:
        with open(output_file, 'w') as f:
            json.dump(output_data, f)
        print(f"Processed data written to: {output_file}")
    except Exception as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    main()