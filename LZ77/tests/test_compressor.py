import pytest
import os
import LZ77.compressor

class TestCompressor(object):
    def test_compress(self):
        input_file = os.path.join('data', 'tests', 'test_data.txt')
        output_path = os.path.join('data', 'tests', 'compressed')
        output_file = LZ77.compressor.compress(input_file, output_path)
        assert os.path.exists(output_file)
        assert os.path.isfile(output_file)
        assert os.stat(output_file).st_size <= os.stat(input_file).st_size