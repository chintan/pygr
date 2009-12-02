
from pygr.sequence import *

from pygr import seqdb

def main():
    """This function does something.
    Example:
    >>> main()
    24
    """
    sp = seqdb.SequenceFileDB('data/sp_hbb1')
    
    print len(sp)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
