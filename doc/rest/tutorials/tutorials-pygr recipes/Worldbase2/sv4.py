
from pygr import worldbase, metabase

from pygr import seqdb, sqlgraph

def main():
    """This function returns the argument.
    Example:
    >>> main()
    """
    serverInfo = sqlgraph.DBServerInfo(host='genome-mysql.cse.ucsc.edu',user='genome')

    mrna = sqlgraph.SQLTable('hg18.knownGeneMrna', serverInfo=serverInfo,itemClass=UCSCmRNA, itemSliceClass=seqdb.SeqDBSlice)

    # Now we can have both the databases

    serverInfo.__doc__ = 'MySQL server with UCSC genome annotations'

    worldbase.Bio.MSA.UCSC.genome_mysql = serverInfo

    mrna.__doc__ = 'hg18.knownGeneMrna sequence database'
 
    worldbase.Bio.MSA.UCSC.hg18.knownGeneMrna = mrna

    worldbase.commit()

if __name__ == '__main__':
        import doctest
        doctest.testmod()



