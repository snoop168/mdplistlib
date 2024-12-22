# mdplistlib

`mdplistlib` is a Python library for parsing DEBA/MDPLIST files, a format found in iOS filesystems. The library provides an easy-to-use interface for reading and extracting data from these binary files.

See blog article at https://bluecrewforensics.com/2024/12/03/deba-mdplist-files/

---

## Installation

You can install `mdplistlib` via pip:

```bash
pip install mdplistlib
```

## Usage

### Parse File
```python
import mdplist


# Load a file and parse its contents
parsed_data = mdplist.load("example.mdplist")
print(parsed_data)
```

### Parse Raw Bytes
```python
import mdplist

with open('example.file') as file:
    # extract the data from the file or some other nested file structure
    data = file.read(250) #binary data should begin with 0xDEBA0001
    
    # Load a file and parse its contents
    parsed_data = mdplist.loads(data)
    print(parsed_data)

```

## Command Line Usage

### Parse File
```bash
python mdplist_cli.py /path/to/file.mdplist
```

Above command will create a new file at `/path/to/file.json`