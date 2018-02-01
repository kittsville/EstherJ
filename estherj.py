import cson
import json

def convert(input, output):
    output.write(json.dumps(cson.loads(input)))
