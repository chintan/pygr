
from pygr import worldbase

from pygr import seqdb

from pygr import metabase

def main():
    """This function returns the argument.
    Example:
    >>> main()
    """
    mdb = metabase.Metabase('.')

    mdb.Data.Bio.MSA.UCSC.hg18.knownGeneMrna = mrna

    # or mdb.add_resource('Bio.MSA.UCSC.hg18.knownGeneMrna', mrna)

    mdb.commit()   


if __name__ == '__main__':
        import doctest
        doctest.testmod()



