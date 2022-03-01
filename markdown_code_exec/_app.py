import argparse
from markdown_code_exec import parse_text
import sys

def app():
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str,
                        help='input markdown file')
    parser.add_argument('-o', '--output', type=str,
                        help='output markdown file')
    args = parser.parse_args()
    path_in = args.input
    path_out = args.output
    # If no input file was specified ...
    if path_in is None:
        # read from the standard input
        md_in = ''
        for line in sys.stdin:
            md_in += line
    else:
        # else read from the input file
        with open(path_in) as fd:
            md_in = fd.read()
    # Do the actual parsing
    md_out = parse_text(md_in)
    # If no output file was specified ...
    if path_out is None:
        # write to the standard output
        print(md_out)
    else:
        # else write to the output file
        with open(path_out, 'w') as fd:
            fd.write(md_out)
    
