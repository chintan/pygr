
from pygr import worldbase

from pygr import seqdb

from pygr import cnestedlist

from pygr import worldbase # module provides access to our data namespace

def main():
    """This function returns the argument.
    Example:
    >>> main()
    54 
    """

    nlmsa = cnestedlist.NLMSA('/loaner/ucsc17')

    for resID,genome in nlmsa.seqDict.prefixDict.items(): # 1st save the genomes
        genome.__doc__ = 'genome sequence ' + resID
        worldbase.add_resource('Bio.Seq.Genome.' + resID, genome)

    nlmsa.__doc__ = 'UCSC 17way multiz alignment, rooted on hg17'

    worldbase.Bio.MSA.UCSC.hg17_multiz17way = nlmsa

    worldbase.commit() # save all pending data to the metabase

    mm7 = worldbase.Bio.Seq.Genome.mm7() # access our mouae genome

    print len(mm7) # to check

if __name__ == '__main__':
        import doctest
        doctest.testmod()



