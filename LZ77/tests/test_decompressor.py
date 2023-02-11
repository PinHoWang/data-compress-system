import pytest
import os
import LZ77.compressor
import LZ77.decompressor
import filecmp

class TestDecompressor(object):
    def test_decompress(self):
        input_file = os.path.join('data', 'tests', 'test_data.txt')
        output_path = os.path.join('data', 'tests', 'compressed')
        output_file = LZ77.compressor.compress(input_file, output_path)
        
        compressed_input_file = os.path.join('data', 'tests', 'compressed', 'compressed_tests')
        decompressed_output_path = os.path.join('data', 'tests', 'decompressed')
        decompressed_output_file = LZ77.decompressor.decompress(compressed_input_file, decompressed_output_path)
        assert os.path.exists(decompressed_output_file)
        assert os.path.isfile(decompressed_output_file)
        assert filecmp.cmp(input_file, decompressed_output_file) # Compare decompressed file is same as original input file