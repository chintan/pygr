
from pygr import sqlgraph

from pygr import mapping

serverInfo = sqlgraph.DBServerInfo(host='genome-mysql.cse.ucsc.edu', user='genome')

genes = sqlgraph.SQLTable('hg18.knownGene', serverInfo=serverInfo)

refseq = sqlgraph.SQLTable('hg18.refLink', serverInfo)

refseq_it = iter(refseq)

genes_it = iter(genes)

list1 = [refseq_it.next() for i in range(5)]

list2 = [genes_it.next() for i in range(5)]

m = {}

def main():
    """This function returns the argument.
    Example:
    >>> main()
    """

    for i in range(5):
        m[list1[i]] = list2[i]

    print m[list1[2]]

    m = mapping.Mapping(refseq, genes, filename='mymap.shelve', mode='c')

    for i in range(5):
        m[list1[i]] = list2[i]

    m.close()

    m = mapping.Mapping(refseq, genes, filename='mymap.shelve')

    print m[list1[2]]

if __name__ == '__main__':
        import doctest
        doctest.testmod()
















