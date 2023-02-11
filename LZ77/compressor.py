from bitarray import bitarray
from typing import Union
import LZ77.utility as utils
import os

# Default lookahead buffer size and slide window size for LZ77 algorithm
LOOKAHEAD_BUFFER_SIZE = 15
WINDOW_SIZE = 20

def compress(input_file_path, output_file_path=None) -> Union[str, None]:
    """
    Given input file name and target output path, input file will be compressed to output
    folder by LZ77 algorithm.
    The compressed format is:
    - 0 bit followed by 8 bits when there are no previous matches
    - 1 bit followed by 12 bits (distance and length)

    :param input_file_path: Path of input file
    :param output_file_path: Path of output folder
    :return: returns the path of compressed file or nothing if compression failed
    """
    data = None
    i = 0
    output = bitarray(endian='big')

    # Convert file into bytes data array
    try:
        with open(input_file_path, 'rb') as input_file:
            data = input_file.read()
    except IOError:
        print(f"Could not read the file {input_file_path}")
        raise

    # LZ77 algorithm
    while i < len(data):
        longest_match = utils.getLongestMatch(data, i, LOOKAHEAD_BUFFER_SIZE, WINDOW_SIZE)

        if longest_match:
            (match_distance, match_length) = longest_match

            # Add encode data into output
            output.append(True) # Flag for encode data
            # Use frombytes() method to append bytes into output buffer
            output.frombytes(bytes([match_distance >> 4]))
            output.frombytes(bytes([((match_distance & 0xf) << 4) | match_length]))
            i += match_length
        else:
            # Add original data into output buffer if there is no match
            output.append(False)
            output.frombytes(bytes([data[i]]))
            i += 1
            
    # Make output buffer as fully binary array
    output.fill()

    # Write compression data into output folder
    if output_file_path:
        try:
            compressed_output_path = "compressed_" + input_file_path.split('/')[1].split('.')[0]
            output_filename = os.path.join(output_file_path, compressed_output_path)
            with open(output_filename, 'wb') as newFile:
                newFile.write(output.tobytes())
                print("File was compressed successfully and saved to output path...")
                return output_filename
        except IOError:
            print("Could not write to output file path. Please check if the path is correct...")
            raise