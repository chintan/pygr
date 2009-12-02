
from pygr.sequence import *

from pygr import seqdb

def main():
    """This function returns the argument.
    Example:
    >>> main()
    """
    sp = seqdb.SequenceFileDB('data/sp_hbb1') 
    
    pagbo = sp['HBB1_PAGBO']
    
    t = pagbo[20:-30]
   
    idDict = ~sp
    
    sp.close() # to close seqdb.SequenceFileDB after the usage
 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
