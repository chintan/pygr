
from pygr.sequence import *

from pygr import seqdb

def main():
    """This function return the argument.
    Example:
    >>> main()
    146
    VEWTDKERSIISDIFSHLDYEDIGPKALSRCLIVYPWTQRHFSGFGNLYNAESIIGNANVAAHGIKVLHGLDRGLKNMDNIEATYADLSTLHSEKLHVDPDNFKLLADCITIVLAAKMGQAFTAEIQGAFQKFLAVVVSALGKQYH

    """
    sp = seqdb.SequenceFileDB('data/sp_hbb1')
    
    pagbo = sp['HBB1_PAGBO']
    
    print len(pagbo) 

    print pagbo

if __name__ == "__main__":
    import doctest
    doctest.testmod()
