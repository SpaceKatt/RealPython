import argparse, os, sys

"""

This Module is a collection of commands that will
make my life easier:
    
    Usage:
        
    # Not like this: python module.py [argument list]
    Run script, use raw_input prompt
    
    Arguments:
        
    '-r' ; Replace name
    '-w' ; Remove whitespace on end
    
    Example: (for replacing a name)
    
    python python module.py -r "NamE" "better_name"

"""

#def get_arguments():
#    """
#    From the command line, grab arguments useing argparse.
#    
#    Usage:
#        '-r' ; BADNAME BETTER_NAME
#    
#    And then write test here
#    """
#    # Using argparse to grab from cmmd
#    parser = argparse.ArgumentParser()
#    parser.add_argument("-r", "--replace", type = str, nargs=2,
#                        help='Replace one word with another.')
#    parser.add_argument("-w", "--whitedel", type = None,
#                        help='Delete the whitespace!')
#    parser.add_argument("module", type = str, nargs=1)
#    args = parser.parse_args()
#    
#    check if module exists
#    
#    return args.replace

class myraw(object):
    def __init__(self, values):
        self.values = values
        self.stream = self.mygen()
    def mygen(self):
        for i in self.values:
            yield i
    def readline(self):
        return str(self.stream.next())

def grab_easy_args():
    """
    Uses raw_input to grab instructional arguments.
    
    >>> sys.stdin = myraw(['-r'])
    >>> grab_easy_args() # doctest: +ELLIPSIS
    -r ; replace WORD with BETTER_WORD
    ...
    What is required? '-r'
    >>> sys.stdin = sys.__stdin__
    """ 
    r = '-r ; replace WORD with BETTER_WORD'
    w = '-w ; coming soon\n'
    cmd_list = [r, w]
    for i in cmd_list:
        print i
    prompt = "What is required? "
    args = raw_input(prompt)
    return args

def grab_replace():
    """
    >>> sys.stdin = myraw(['wordone', 'wordtwo'])
    >>> grab_replace()
    --> What is the bad name?--> What is the better name?('wordone', 'wordtwo')
    >>> sys.stdin = sys.__stdin__
    """
    bad = raw_input("--> What is the bad name?")
    better = raw_input("--> What is the better name?")
    return bad, better

def grab_name():
    """
    >>> sys.stdin = myraw(['misc/cleaner.py'])
    >>> grab_name()
    --> What is the module name? 'misc/cleaner.py'
    >>> sys.stdin = sys.__stdin__
    """
    name = raw_input("--> What is the module name? ")
    return name

def find_file(name):
    """
    Finds and returns the location of a python module.
    
    >>> print find_file("cleaner.py") # doctest: +ELLIPSIS
    /.../RealPython/misc/cleaner.py
    >>> print find_file("prtone/capitals.py") # doctest: +ELLIPSIS
    /.../RealPython/prtone/capitals.py
    """
    path = os.path.dirname(os.path.abspath(name))
    path = os.path.join(path, name)
    if not os.path.exists(path):
        sys.exit('{} does not exist.'.format(path))
    return path

def file_data(file):
    """
    Fetch file text, as a list of strings,
    each string is one line of the file.
    
    >>> file_data(find_file("cleaner.py")) # doctest: +ELLIPSIS
    [..., '    doctest.testmod(optionflags=doctest.ELLIPSIS)']
    """
    with open(file, 'r') as f:
        text = list(f)
    return text

def do_replace(bad, better):
    """
    Once list of code lines has been gathered,
    we now replace the undesirable word with a better word.
    Then, we return the transformed list.

    Maybe add a search for lines that actually have bad word?
    Find a way to find module from name
    """
#    list_code = file_data(module_name)
    pass

def write_processed_to_file(code_list, file):
    """Writes list of replacements to *.py file."""
    pass

def do_stuff():
    """Does the stuff to do the thing."""
    module_location = find_file(grab_name())
    args = list(grab_easy_args())
    data = file_data(module_location)
    if 'r' in args:
        bad, better = grab_replace()
        do_replace(bad, better)
    print args
    write_processed_to_file(data, module_location)
    
#do_stuff()
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)