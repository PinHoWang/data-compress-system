from typing import Union

def getLongestMatch(data, position, lookahead_buffer_size, window_size) -> Union[tuple, None]:
        """
        Find the longest match to a substring starting at the position
        in the lookahead buffer from the history window
        """

        end_of_buffer = min(position + lookahead_buffer_size, len(data)+1)

        match_distance = -1
        match_length = -1

        for j in range(position + 2, end_of_buffer):
            start_index = max(0, position - window_size)
            substring = data[position:j]

            for i in range(start_index, position):
                repetitions = len(substring) // (position - i)
                last = len(substring) % (position - i)

                matched_string = data[i:position] * repetitions + data[i:i+last]

                if matched_string == substring and len(substring) > match_length:
                    match_distance = position - i
                    match_length = len(substring)

        if match_distance > 0 and match_length > 0:
            return (match_distance, match_length)
        else:
            return None