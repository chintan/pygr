
from pygr.sequence import *

from pygr import seqdb

def main():
    """This function does something.
    Example:
    >>> main()
    HBB1_PAGBO
    <SequenceFileDB 'data/sp_hbb1'>
    True
    """
    sp = seqdb.SequenceFileDB('data/sp_hbb1') 
    
    pagbo = sp['HBB1_PAGBO']
    
    t = pagbo[20:-30]
   
    print t.id
   
    print t.db

    print t.db is sp
 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
