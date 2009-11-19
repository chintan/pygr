
from pygr.sequence import *

from pygr import seqdb

def main():
    """This function does something.
    Example:
    >>> main()
    96
    False
    True
    20 116 1
    """
    s = Sequence('attatatgccactat','bobo') #creating a sequence named bobo

    sp = seqdb.SequenceFileDB('data/sp_hbb1') 
    
    pagbo = sp['HBB1_PAGBO']
    
    t = pagbo[20:-30]
   
    print len(t)
    
    print t in s

    print t in pagbo

    print t.start, t.stop, t.orientation

 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
