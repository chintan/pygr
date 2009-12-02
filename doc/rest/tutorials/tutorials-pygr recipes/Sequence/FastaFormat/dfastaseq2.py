
from pygr.sequence import *

from pygr import seqdb

def main():
    """This function return the argument.
    Example:
    >>> main()
    146
    ['HBB0_PAGBO', 'HBB1_ANAMI', 'HBB1_CYGMA', 'HBB1_IGUIG', 'HBB1_MOUSE', 'HBB1_ONCMY', 'HBB1_PAGBO', 'HBB1_RAT', 'HBB1_SPHPU', 'HBB1_TAPTE', 'HBB1_TORMA', 'HBB1_TRICR', 'HBB1_UROHA', 'HBB1_VAREX', 'HBB1_XENBO', 'HBB1_XENLA', 'HBB1_XENTR', 'MYG_DIDMA', 'MYG_ELEMA', 'MYG_ERIEU', 'MYG_ESCGI', 'MYG_GALCR', 'PRCA_ANASP', 'PRCA_ANAVA']
         """
    sp = seqdb.SequenceFileDB('data/sp_hbb1')
    
    print len(sp)

    print sp.keys()
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
