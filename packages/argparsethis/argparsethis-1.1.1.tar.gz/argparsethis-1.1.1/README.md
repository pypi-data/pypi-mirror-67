# argparsethis

A drop-in replacement to Python's built-in argparse, that provides the capability to argparse *any* arbitrary string, not just command line arguments. Is sourced from https://github.com/python/cpython/blob/3.8/Lib/argparse.py.

## Usage
When creating your ArguementParser, just override the parameter `input_list`  as a list of strings to parse. We recommend using `shlex` to split any raw strings into a list correctly. If `input_list` is not overridden, it will use standard command line arguments like normal

```
import shlex
import argparsethis as argparse

# Argument parsing which outputs a dictionary.
def parse_args(input_str):
    #Setup the argparser and all args
    input_list = shlex.split(input_str)
    parser = argparse.ArgumentParser(input_list = input_list)
    parser.add_argument("-q", "--quiet", help="suppress extra output", action="store_true", default=False)
    return parser.parse_args()

argv1 = parse_args("test -h")
argv2 = parse_args("test -q")

if not argv2.quiet:
    print("LOUD NOISES")
```
