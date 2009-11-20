from pygr import sqlgraph, seqdb, annotation

serverInfo = sqlgraph.DBServerInfo(host='genome-mysql.cse.ucsc.edu', user='genome')


def main():
    """This function returns argument.
    Example:
    >>> main()
    66803
    ['name', 'chrom', 'strand', 'txStart', 'txEnd', 'cdsStart', 'cdsEnd', 'exonCount', 'exonStarts', 'exonEnds', 'proteinID', 'alignID']
    None
    'chr1'
    55424L
    59692L
    '+'
    """

    genes = sqlgraph.SQLTable('hg18.knownGene', serverInfo = serverInfo)

    print len(genes)

    print genes.columnName

    print genes.primary_key

    genes.primary_key = 'name'

    tx = genes['uc009vjh.1']

    genes = sqlgraph.SQLTable

    print tx.chrom

    print tx.txStart

    print tx.txEnd

    print tx.strand


if __name__ == '__main__':
    import doctest
    doctest.testmod()