import os
from bitarray import bitarray
from typing import Union

def decompress(input_file_path, output_file_path=None) -> Union[str, None]:
    """
    Given a string of the compressed file path, the data is decompressed back to its 
    original form, and written into the output file path if provided. If no output 
    file path is provided, the decompressed data is returned as a string
    """
    data = bitarray(endian='big')
    output_buffer = []

    try:
        with open(input_file_path, 'rb') as input_file:
            data.fromfile(input_file)
    except IOError:
        print('Could not open input file...')
        raise
    
    while len(data) >= 9:
        flag = data.pop(0)
        if not flag:
            byte = data[0:8].tobytes()
            output_buffer.append(byte)
            del data[0:8]
        else:
            byte1 = ord(data[0:8].tobytes())
            byte2 = ord(data[8:16].tobytes())

            del data[0:16]
            distance = (byte1 << 4) | (byte2 >> 4)
            length = (byte2 & 0xf)

            for i in range(length):
                output_buffer.append(output_buffer[-distance])
    out_data = b''.join(output_buffer)
    
    if output_file_path:
        try:
            decompressed_output_path = "decompressed_" + input_file_path.split('/')[1].split('.')[0] + ".txt"
            output_filename = os.path.join(output_file_path, decompressed_output_path)
            with open(output_filename, 'wb') as newFile:
                newFile.write(out_data)
                print('File was decompressed successfully and saved to output path...')
                return output_filename
        except IOError:
            print('Could not write output file path. Please check if the path is correct...')
            raise