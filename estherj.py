import cson
import json
import sys

def convert(input, output):
    output.write(json.dumps(cson.load(input)))

if __name__ == '__main__':
    convert(sys.stdin, sys.stdout)
