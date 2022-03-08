# markdown_code_exec

*Execute Python code in Markdown files and captures the output*

Copyright 2022 Sebastiaan Mathôt


## Function reference

``` { .python silent }
from markdown_code_exec import parse_text, parse_file
from npdoc_to_md import render_md_from_obj_docstring

print(render_md_from_obj_docstring(parse_text, 'markdown_code_exec.parse_text'))
print('\n\n')
print(render_md_from_obj_docstring(parse_file, 'markdown_code_exec.parse_file'))
```

## License

GNU General Public License 3
