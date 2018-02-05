import cson
import json
import sys

def convert(input, output):
    output.write(json.dumps(cson.load(input)))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise TypeError("Missing CSON file path")

    filePath = sys.argv[1]

    with open(filePath, 'r') as csonFile:
        convert(csonFile, sys.stdout)
