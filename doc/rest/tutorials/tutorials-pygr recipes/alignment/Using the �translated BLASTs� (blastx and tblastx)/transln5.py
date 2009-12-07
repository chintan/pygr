
from pygr import seqdb

from pygr import blast

from pygr import cnestedlist

from pygr import annotation

#from pygr import translationdb

def main():
    """This function returns argument
    Example:
    >>> main()
    [HBB_MUSGR[0:52], HBB_SQUAC[0:52], HBB2_TORMA[0:52]]
    gi|171854975|dbj|AB364477.1|[0:156] aligns to HBB_MUSGR[0:52]
    M  V  H  W  T  Q  E  E  R  D
    """

    dna_db = seqdb.SequenceFileDB('data/hbb1_mouse.fa')

    dna_seq = dna_db['gi|171854975|dbj|AB364477.1|']

    prot_db = seqdb.SequenceFileDB('data/sp_all_hbb')

    blastmap = blast.BlastxMapping(prot_db)

    results = blastmap[dna_seq]

    frame0_results = results[frame0]

    print frame0_results.keys()[:3]

    src, dest, edge = frame0_results.edges()[0]
 
    print repr(src.sequence), 'aligns to', repr(dest)

    aa = '  '.join(str(dest[:10]))

    print "%s\n%s" % (src.sequence[:30], aa)

if __name__ == '__main__':
    import doctest
    doctest.testmod()










