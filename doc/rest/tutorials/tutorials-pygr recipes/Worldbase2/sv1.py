
from pygr import worldbase

from pygr import seqdb

hg17 = seqdb.SequenceFileDB('hg17') # human genome sequence

hg17.__doc__ = 'human genome sequence draft 17' # required!

worldbase.Bio.Seq.Genome.HUMAN.hg17 = hg17 # save as this name

worldbase.commit() # save all pending data to the metabase

hg17 = worldbase.Bio.Seq.Genome.HUMAN.hg17() # find the resource

 
if __name__ == '__main__':
        import doctest
        doctest.testmod()



