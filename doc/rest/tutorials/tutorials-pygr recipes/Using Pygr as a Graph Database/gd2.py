
import os

import MySQLdb # standard module for accessing MySQL, now get a cursor...

from pygr.seqdb import *   # pygr module for working with sequences from databases

def main():
    """This function returns the argument.
    Example:
    >>> main()
    MySQL
    'acctgggtgatgaaataaatttttacgccaaatcccgatgacacacaatt'
    """
    rdb = MySQLdb.connect(db='HUMAN_SPLICE_03',read_default_file = os.environ['HOME']+'/.my.cnf')

    t = SQLTable('genomic_cluster_JUN03',rdb.cursor()) #interface to a table of sequences

    t.objclass(DNASQLSequence) #use this class as "row objects"

    s2 = t['Hs.1162'] # get a specific sequence object by ID

    print str(s2[1000:1050])

if __name__ == '__main__':
        import doctest
        doctest.testmod()

 