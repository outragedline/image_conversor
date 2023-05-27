#!/bin/python
import sys
import os
import subprocess

path = sys.argv[1]

if not os.path.isdir(path):
    print("Directory doesn't exist")
    sys.exit(1)

def convert(source_directory):
    output_dir = os.path.join(os.getcwd(), "converted")

    for root, dirs, files in os.walk(source_directory):
        relative_path = os.path.relpath(root, source_directory)
        target_dir = os.path.join(output_dir, relative_path)
        os.makedirs(target_dir, exist_ok=True)

    for root, dirs, files in os.walk(source_directory):
        relative_path = os.path.relpath(root, source_directory)
        target_dir = os.path.join(output_dir, relative_path)
        for file in files:
            output_file_name = os.path.splitext(file)[0]
            output_file_path = os.path.join(target_dir, output_file_name + ".jpg")
            input_file_path = os.path.join(root, file)
            subprocess.run(['ffmpeg', '-i', input_file_path, output_file_path])

convert(path)
