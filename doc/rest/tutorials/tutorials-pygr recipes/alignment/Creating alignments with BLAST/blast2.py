
from pygr import seqdb

from pygr import blast

def main():
    """This function returns argument
    Example:
    >>> main()
    gapped[0:40] matches ungapped[0:40]
    gapped[44:74] matches ungapped[40:70]
    ungapped[0:40] matches gapped[0:40]
    ungapped[40:70] matches gapped[44:74]
    """
    db = seqdb.SequenceFileDB('data/gapping.fa')

    blastmap = blast.BlastMapping(db)

    ungapped = db['ungapped']

    gapped = db['gapped']

    slice = blastmap[gapped]

    edges = slice.edges()

    al = blastmap(queryDB=db)
    for seq in db.values():
        for (src, dest, edge) in al[seq].edges():
            print repr(src), 'matches', repr(dest)

if __name__ == '__main__':
    import doctest
    doctest.testmod()










