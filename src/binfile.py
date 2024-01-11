import os
import sys


class BinaryFileConverter:
    def __init__(self):
        pass

    def __file_to_binary_string(self, file_path):
        with open(file_path, 'rb') as file:
            binary_code = file.read()
            binary_string = ''.join(format(byte, '08b') for byte in binary_code)

    def __binary_string_to_file(self, binary_string, file_path):
        with open(file_path, 'wb') as file:
            bytes_list = [int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8)]
            bytes_arr = bytearray(bytes_list)
            file.write(bytes_arr)
