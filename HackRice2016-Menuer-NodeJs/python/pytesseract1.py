"""
Module that parses the text in an image
"""

import argparse
import subprocess


def execute_cmd(cmd):
    """
    Help function that executes a command in the terminal
    """
    return subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]


def main():
    """
    Top level function
    """
    # arg parser
    parser = argparse.ArgumentParser(description='Python Image Text Parser v1')
    parser.add_argument('-f', required=True, help='image file directory')
    parser.add_argument('-t', default=None, help='image file directory')
    args = parser.parse_args()
        
    # retrieve the file name
    file_name = args.f
    tesseract = "/opt/local/bin/tesseract" if args.t is None else args.t
    
    # build up command line
    cmd = [tesseract, file_name, "stdout"]
    
    # print output to stdout
    print execute_cmd(cmd)
    



if __name__ == "__main__":
    main()