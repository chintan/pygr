
from pygr import sqlgraph

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


    liteserver = sqlgraph.SQLiteServerInfo('mapping.sqlite')

    m = sqlgraph.SQLTable('refseq_knowngene', serverInfo=liteserver, writeable=True, createTable = 'CREATE TABLE refseq_knowngene (refseq_id VARCHAR(40) PRIMARY KEY, kg_id VARCHAR(40) NOT NULL, INDEX(kg_id));')

    for i in range(5):
        m.new(refseq_id=list1[i].id, kg_id=list2[i].id)

    m = sqlgraph.MapView(refseq, genes, 'select kg_id from refseq_knowngene where refseq_id=%s', inverseSQL = 'select refseq_id from refseq_knowngene where kg_id = %s')

    print m[list1[1]]

if __name__ == '__main__':
        import doctest
        doctest.testmod()












