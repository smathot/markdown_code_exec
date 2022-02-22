A code snippet like this should not be processed:

```
print('Leave this alone')
```

The `capture` flag indicates that the standard output should be captured and inserted as a new fenced code block below the code.

``` { .python capture }
print('This output should be captured!')
print('This too')
```

The `silent` flag indicates that the code should be replaced by the output.

``` { .python silent }
print('A silent cell')
```

The `exception` flag indicates that the code should raise an `Exception`. The traceback is then inserted instead of the standard output.


``` { .python capture exception }
# A cell that should raise a ValueError
int('x')
```
