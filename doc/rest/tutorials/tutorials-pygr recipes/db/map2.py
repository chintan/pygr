
from pygr import sqlgraph

from pygr import metabase

serverInfo = sqlgraph.DBServerInfo(host='genome-mysql.cse.ucsc.edu', user='genome')

genes = sqlgraph.SQLTable('hg18.knownGene', serverInfo=serverInfo)

refseq = sqlgraph.SQLTable('hg18.refLink', serverInfo)

refseq_it = iter(refseq)

genes_it = iter(genes)

list1 = [refseq_it.next() for i in range(5)]

list2 = [genes_it.next() for i in range(5)]

m = {}

for i in range(5):
    m[list1[i]] = list2[i]


serverInfo.__doc__ = 'MySQL server with UCSC genome annotations'

worldbase.Bio.MSA.UCSC.genome_mysql = serverInfo

genes.__doc__ = 'UCSC hg18.knownGene database'

worldbase.Test.Annotation.UCSC.hg18.knownGene = genes

refseq.__doc__ = 'UCSC hg18.refseqLink database'

worldbase.Test.Annotation.UCSC.hg18.refseqLink = refseq

m.__doc__ = 'refseq to knownGene mapping'

worldbase.Test.Annotation.UCSC.hg18.refseqToKG = m

worldbase.schema.Test.Annotation.UCSC.hg18.refseqToKG = metabase.OneToOneMapping(refseq, genes, bindAttrs=('gene', 'refseq'))


worldbase.commit()

worldbase.clear_cache()

def main():
    """This function returns the argument.
    Example:
    >>> main()
    """

refseq = worldbase.Test.Annotation.UCSC.hg18.refseqLink()

r = refseq['NM_003710']

print r.gene, r.gene.id

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    







