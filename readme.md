# markdown_code_exec

*Execute Python code in Markdown files and captures the output*

Copyright 2022 Sebastiaan Mathôt

## Command-line usage

usage: markdown_code_exec.py [-h] [-i INPUT] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input markdown file
  -o OUTPUT, --output OUTPUT
                        output markdown file


## Function reference

**<span style="color:purple">markdown&#95;code&#95;exec.parse&#95;text</span>_(md)_**


Takes a `str` containing markdown text, finds code blocks in the
markdown, executes these code blocks and captures the output, and then
embeds the captured output in the markdown.


#### Parameters
* md: str :  The input markdown string

#### Returns
<b><i>str</i></b>  The compiled markdown string



**<span style="color:purple">markdown&#95;code&#95;exec.parse&#95;file</span>_(src, dst)_**


Takes a markdown input file, executes code blocks while capturing output
and writes the result to a new output file.


src: str
    The full path to the input file
dst: str
    The full path to the output file

## License

GNU General Public License 3
