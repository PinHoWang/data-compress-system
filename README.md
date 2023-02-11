# Data Compression Design
In this coding exercise, the **LZ77 lossless compression algorithm** will be introduced to compress data buffer of bytes.
## Assumptions
1. Data is an array of bytes. Each byte will contain a number from 0 to 127 (0x00 to 0x7F). It is common for the data in the buffer to have the same value repeated in the series.
2. Raw data has already done the data cleaning.
2. The compressed data will need to be decompressable.

## Goals
- Compression/decompression algorithm
- Less number of bytes the output uses if saved to file
- Runtime
- Scalability
- Maintainability
- Testability

## Algorithm
For the algorithm, because we assume the data in buffer has the same value repeated in the series, e.g. [1, 1, 1, 2, 3, 3, 3, ...]. LZ77 algorithm becomes a great candidate for this problem. LZ77 compression algorithm is lossless compression algorithm and it reduces the size of the input data by replacing redundant information with length-distance pair. <br/>
We compare the data in slide-window and lookahead buffer to find out the longest repeated substring, and replace with its length-distance pair. <br/>
### Steps of the algorithm:
1. Set a fixed size of slide window and lookahead buffer (default slide window size is 20, lookahead buffer is 15).
2. Find the longest repeated substring between slide window and lookahead buffer.
3. If there is a match substring, we can encode the data into length-distance pair and add into output string. If not, we can just add original data into output string. (Need flag to determine whether it's encoded or not)
4. Move the slide window and lookahead buffer forward (if there is a match in step 3, move forward as the length of the encode, otherwise, 1)
5. Start again from step 2 until we move to end of the data

## Folder Structure
    .
    |-- data
        |-- tests               # Tests data
            |-- compressed      # Compressed tests data
            |-- decompressed    # Decompressed tests data
        |-- compressed          # Compressed data from the algorithm
    |-- LZ77                    # LZ77 algorithm
        |-- tests               # Unittests for LZ77 algorithm
        |-- compressor.py       # Implementation of compression algorithm
        |-- decompressor.py     # Implementation of decompression algorithm
        |-- utility.py          # Utils
    |-- compress.py             # Executable file for compression
    |-- README
    |-- requirements.txt


## Usage
### Requirements
- Python3

### Install the dependency
```
pip3 install -r requirements.txt
```

### Run compression algorithm
```
./compress.py <target file>
```
e.g.
```
./compress.py data/data1.txt
```
Output compressed file will be generated in ```data/compressed``` folder <br/>
Run ```./compress.py -h``` for more details.

### Run decompression algorithm
```
./decompress.py <target compressed file>
```
e.g.
```
./decompress.py data/compressed/compressed_data1
```
Run ```./decompress.py -h``` for more details.

### Hints
If ```compress.py``` and ```decompress.py``` file can't be executed, you may need to run
```
chmod +x compress.py decompress.py
```

## Tests
Run LZ77 unittests
```
python3 -m pytest
```


## Results
After running the algorithm, the compressed file will be generated, there is also a comparasion of original file size and compressed file size showing in the console. <br/>
![alt text](TODO)

## Conclusion
- We can successfully compress and decompress the target file
- Size of the compressed file is less number of bytes than original file
- The LZ77 algorithm, utility functions, and main function are decoupled for scalability and flexiablity
- Unittests are covered for testability