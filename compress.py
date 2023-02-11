#!/usr/bin/env python3
import argparse
import os
import sys
import LZ77.compressor

'''
This script is for executing compression algorithm via command line interface
'''

# Command line parser
parser = argparse.ArgumentParser(description='Compress a file')
parser.add_argument('input_file', help='input file to be compressed')
args = parser.parse_args()

# Main script
input_file = args.input_file

if not os.path.isfile(input_file):
    print(f"ERROR: {input_file} doesn't exist")
    sys.exit(1)

uncompressed_size = os.stat(input_file).st_size
print(f"Uncompressed size: {uncompressed_size} bytes.")

# execute the compression algorithm
output_file = ''
output_file = LZ77.compressor.compress(input_file, 'data/compressed/')

compressed_size = os.stat(output_file).st_size
print(f"Compressed size: {compressed_size} bytes")
print(f"Compression ratio = {uncompressed_size} / {compressed_size} = {uncompressed_size / compressed_size}")
sys.exit(0)