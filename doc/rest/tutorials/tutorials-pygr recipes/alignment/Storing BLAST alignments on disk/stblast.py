
from pygr import seqdb

from pygr import blast

from pygr import cnestedlist

def main():
    """This function returns argument
    Example:
    >>> main()
    gapped[0:40] matches ungapped[0:40]
    gapped[44:74] matches ungapped[40:70]
    """
    db = seqdb.SequenceFileDB('data/gapping.fa')
  
    blastmap = blast.BlastMapping(db)

    store_al = cnestedlist.NLMSA('tempdir/blastn',mode='w', pairwiseMode=True, bidirectional=False)

    _ = blastmap(queryDB=db, al=store_al)

    store_al.build(saveSeqDict=True)
  
    del store_al

    loaded_al = cnestedlist.NLMSA('tempdir/blastn')

    db = loaded_al.seqDict

    g = db['gapping.gapped']

    edges = loaded_al[g].edges()
        
    for (src, dest, edge) in edges:
        print repr(src), 'matches', repr(dest)

if __name__ == '__main__':
    import doctest
    doctest.testmod()










