"""
This Module is a collection of commands that will
make my life easier:

    Usage:

    Run script, use raw_input prompt

    Arguments:

    '-r' ; Replace name
    '-w' ; Remove whitespace on end

    Example: (for replacing a name, 'topdir' with 'search_start')

    $ python cleaner.py
    >>> sys.stdin = MyRaw(['misc.py', 'r', 'topdir', 'search_start'])
    >>> do_stuff() # doctest: +ELLIPSIS
    --> What is the module name? -r ; replace WORD with BETTER_WORD
    -w ; coming soon
    <BLANKLINE>
    What is required?--> What is the bad name?--> What is the better name?-
    >>> sys.stdin = sys.__stdin__
"""
import os, sys

class MyRaw(object):
    """Feeds input into raw_input during doctesting."""
    def __init__(self, values):
        self.values = values
        self.stream = self.mygen()
    def mygen(self):
        """Generates values when needed."""
        for i in self.values:
            yield i
    def readline(self):
        """Need to look up why this one works."""
        return str(self.stream.next())

def grab_easy_args():
    """
    Uses raw_input to grab instructional arguments.

    >>> sys.stdin = MyRaw(['-r'])
    >>> grab_easy_args() # doctest: +ELLIPSIS
    -r ; replace WORD with BETTER_WORD
    ...
    What is required?-'-r'
    >>> sys.stdin = sys.__stdin__
    """
    replace = '-r ; replace WORD with BETTER_WORD'
    whitespac = '-w ; coming soon\n'
    cmd_list = [replace, whitespac]
    for i in cmd_list:
        print i
    prompt = "What is required?-"
    args = raw_input(prompt)
    return args

def grab_replace():
    """
    >>> sys.stdin = MyRaw(['wordone', 'wordtwo'])
    >>> grab_replace()
    -> What is the bad name?--> What is the better name?-('wordone', 'wordtwo')
    >>> sys.stdin = sys.__stdin__
    """
    bad = raw_input("-> What is the bad name?-")
    better = raw_input("-> What is the better name?-")
    return bad, better

def grab_name():
    """
    >>> sys.stdin = MyRaw(['misc/cleaner.py'])
    >>> grab_name()
    --> What is the module name? 'misc/cleaner.py'
    >>> sys.stdin = sys.__stdin__
    """
    name = raw_input("--> What is the module name? ")
    return name

def find_file(file_name, topdir):
    """
    Finds and returns the location of a python module.

    >>> path =  find_file("cleaner.py", '..')
    >>> print path # doctest: +ELLIPSIS
    /.../RealPython/misc/cleaner.py
    >>> os.path.exists(path)
    True
    >>> print find_file('alalalgd', '..')
    None
    """
    for dirpath, dirnames, files in os.walk(topdir):
        del dirnames
        for name in files:
            path = os.path.join(dirpath, name)
            if file_name in path and path.endswith(".py"):
                return os.path.abspath(path)
            else:
                pass

def get_path():
    """
    Facilitates the process of getting the file path.

    >>> sys.stdin = MyRaw(['misc/cleaner.py'])
    >>> get_path() # doctest: +ELLIPSIS
    --> ... '/.../RealPython/misc/cleaner.py'
    >>> sys.stdin = sys.__stdin__
    """
    file_name = grab_name()
    path = find_file(file_name, '..')
    if path == None:
        path = find_file(file_name, '/')
    if not os.path.exists(path):
        sys.exit('{} does not exist.'.format(path))
    return path

def file_data(input_file):
    """
    Fetch file text, as a list of strings,
    each string is one line of the file.

    >>> file_data(find_file("cleaner.py", '..')) # doctest: +ELLIPSIS
    [..., '    doctest.testmod(optionflags=doctest.ELLIPSIS)\\n']
    """
    with open(input_file, 'r') as filz:
        text = list(filz)
    return text

def do_replace(text_list, bad, better):
    """
    Once list of code lines has been gathered,
    we now replace the undesirable word with a better word.
    Then, we return the transformed list.

    >>> bar = ['foo this is a string in a list.']
    >>> do_replace(bar, 'foo', 'Yup,')
    ['Yup, this is a string in a list.']
    """
    new_list = []
    for line in text_list:
        line = line.replace(bad, better)
        new_list.append(line)
    return new_list

def write_processed_to_file(code_list, input_file):
    """Writes list of code to *.py file."""
    with open(input_file, 'w') as fil:
        for line in code_list:
            fil.write(line)

def do_stuff():
    """Does the stuff to do the thing."""
    module_location = get_path()
    args = list(grab_easy_args())
    data = file_data(module_location)
    if 'r' in args:
        bad, better = grab_replace()
        stuff = do_replace(data, bad, better)
    if 'w' in args:
        pass # should take out if statements into new function
    write_processed_to_file(stuff, module_location)

do_stuff()

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
