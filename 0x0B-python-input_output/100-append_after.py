#!/usr/bin/python3
"""
Function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Module to append after certain strings"""
    with open(filename, 'r+', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
        new_ln = []
        for line in lines:
            new_ln.append(line)
            if search_string in line:
                new_ln.append(new_string)
        f.seek(0)
        f.write('\n'.join(new_ln) + '\n')
