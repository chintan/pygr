
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

    print m[list1[2]]

    kgXref = sqlgraph.MapView(refseq, genes,'select kgID from hg18.kgXref where refseq=%s',inverseSQL='select refseq from hg18.kgXref where kgID=%s')

    g = kgXref[r]


    kgXref.__doc__ = 'refseq to knownGene mapping'

    worldbase.Test.Annotation.UCSC.hg18.refseqToKG = kgXref

    worldbase.schema.Test.Annotation.UCSC.hg18.refseqToKG = metabase.OneToOneMapping(refseq, genes, bindAttrs= ('gene', 'refseq'))

    worldbase.commit()

    worldbase.clear_cache()

    genes = worldbase.Test.Annotation.UCSC.hg18.knownGene()

    g = genes['SOME ID']

    print g.refseq, g.refseq.id

if __name__ == '__main__':
        import doctest
        doctest.testmod()
















