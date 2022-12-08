# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 16:31:43 2022

@author: Sven
"""

def framed_print(input_str, frame_size, frame_symbol="#"):
    """Put your print in the right frame.
    """
    string_length = len(input_str)
    for _ in range(frame_size):
        print((string_length + 2 + 2 * frame_size) * frame_symbol)
        # print actual content
    print(f"{frame_size} * {frame_symbol} {input_str} {frame_size} * {frame_symbol}")
    for _ in range(frame_size):
        print((string_length + 2 + 2 * frame_size) * frame_symbol)



framed_print("yes this look awesome!", 3, ">")