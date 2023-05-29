# if extension has preload.py file in its root directory, it is loaded before parsing commandline args
# if extension's preload.py has a preload function, 
# it is called, and commandline args parser is passed to it as an argument. 
# Here's an example of how to use it to add a command line argument:

def preload(parser):
    parser.add_argument("--wildcards-dir", type=str, help="directory with wildcards", default=None)