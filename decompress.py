#!/usr/bin/env python3
import argparse
import os
import sys
import LZ77.decompressor

'''
This script is for executing compression algorithm via command line interface
'''

# Command line parser
parser = argparse.ArgumentParser(description='Decompress a file')
parser.add_argument('input_file', help='input file to be decompressed')
args = parser.parse_args()

# Main script
input_file = args.input_file

if not os.path.isfile(input_file):
    print(f"ERROR: {input_file} doesn't exist")
    sys.exit(1)

# execute the decompression algorithm
output_file = ''
output_file = LZ77.decompressor.decompress(input_file, 'data/decompressed/')
print(f"Successfully decompressed the file to {output_file}...")
sys.exit(0)