import re
import io
import os
import sys

PATTERN = r'^```\s*{(?P<attr>[. a-zA-Z0-9_]+)}\s*\n(?P<code>.*?)\n```\s*$'


def parse_text(md):
    workspace = {}
    md_out = md
    offset = 0
    for match in re.finditer(PATTERN, md, re.MULTILINE | re.DOTALL):
        attr = match.group('attr').split()
        # Only process code blocks with capture or silent attributes
        if 'capture' not in attr and 'silent' not in attr:
            continue
        # Execute the code block, and capture all the output that was generated
        if 'exception' in attr:
            try:
                exec(match.group('code'), workspace)
            except Exception as e:
                output = str(e)
            else:
                raise ValueError('an expected Exception didn\'t occur')
        else:
            output_buffer = io.StringIO()
            sys.stdout = output_buffer
            exec(match.group('code'), workspace)
            sys.stdout = sys.__stdout__
            output = output_buffer.getvalue()
        start = match.start() + offset
        end = match.end() + offset
        if 'capture' in attr:
            output = output.strip()
            insert = f'\n__Out:__\n\n```\n{output}\n```\n'
            md_out = md_out[:end] + insert + md_out[end:]
            offset += len(insert)
            continue
        md_out = md_out[:start] + output + md_out[end:]
        offset = offset + len(output) - end + start
    return md_out


def parse_file(src, dst):
    if not os.path.isfile(src):
        raise ValueError('{} is not a file'.format(src))
    with open(src) as fd:
        md = fd.read()
    md = parse_text(md)
    with open(dst, 'w') as fd:
        fd.write(md)
