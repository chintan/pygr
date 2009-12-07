from pygr import sqlgraph
 
from pygr import seqdb, annotation

from pygr import worldbase

from pygr import cnestedlist

def main():
    """This function returns argument.
    Example:
    >>> main()
    ATGGTGCACCTGACTGATGCTGAGAAGGCTGCTGTCTCTGGCCTGTGGGGAAAGGTGAACTCCGATGAAG
    ATGGTGCACCTGACTGATGCTGAGAAGGCTGCTGTCTCTGatgcGCCTGTGGGGAAAGGTGAACTCCGATGAAG 
                                            ^^^^
    """
    simple_al = cnestedlist.NLMSA('hbb', mode='memory', pairwiseMode=True)

    db = seqdb.SequenceFileDB('data/gapping.fa')
   
    ungapped = db['ungapped']
	
    gapped = db['gapped']

    print ungapped

    print gapped

    print ' '*40 + '^^^^'

if __name__ == '__main__':
    import doctest
    doctest.testmod()











