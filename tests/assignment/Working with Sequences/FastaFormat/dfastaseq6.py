
from pygr.sequence import *

from pygr import seqdb

def main():
    """This function does something.
    Example:
    >>> main()
    HBB1_PAGBO
    """
    sp = seqdb.SequenceFileDB('data/sp_hbb1') 
    
    pagbo = sp['HBB1_PAGBO']
    
    t = pagbo[20:-30]
   
    idDict = ~sp
    
    print idDict[t]
 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
