# EstherJ

[![Build Status](https://travis-ci.org/kittsville/EstherJ.svg?branch=master)](https://travis-ci.org/kittsville/EstherJ)

Converts CSON to JSON using pycson.

# Requirements

- Python 2.7

# Installation

1. Clone/download repo
2. Install dependencies with `pip install -r reequirements.txt`

# Usage

Run from command line using stdin/stdout or import and call yourself:

```python
import estherj

with open('foo.cson') as csonFile:
  with open('bar.json', 'w+') as jsonFile:
    estherj.convert(csonFile, jsonFile)
```
