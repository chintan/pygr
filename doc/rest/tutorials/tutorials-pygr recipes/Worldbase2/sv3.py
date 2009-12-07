
from pygr import worldbase

from pygr import seqdb

from pygr import splicegraph

from pygr.metabase import ManyToManyRelation

def main():
    """This function returns the argument.
    Example:
    >>> main()
    let say 54 to run doctest
    """
    
    splicegraph.__doc__ = 'graph of exon:splice:exon relations in human genes'

    worldbase.Bio.Genomics.ASAP2.hg17.splicegraph = splicegraph # add a new resource

    from pygr.metabase import ManyToManyRelation

    worldbase.schema.Bio.Genomics.ASAP2.hg17.splicegraph = ManyToManyRelation(exons, exons, splices,bindAttrs  = ('next', 'previous', 'exons'))

    worldbase.commit() # save all pending data to the metabase

if __name__ == '__main__':
        import doctest
        doctest.testmod()



