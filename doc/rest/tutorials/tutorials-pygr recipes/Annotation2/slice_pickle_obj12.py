class MySliceInfo(object):
   def __init__(self, seq_id, start, stop, orientation):
      (self.id, self.start, self.stop, self.orientation) = (seq_id, start, stop, orientation)

class MyFunkySliceInfo(object):
   def __init__(self, seq_id, begin, end, strand):
       (self.seq_id, self.begin, self.end, self.strand) = (seq_id, begin, end, strand)

from pygr import seqdb, annotation, worldbase, mapping, cnestedlist, sqlgraph

from slice_pickle_obj import MySliceInfo, MyFunkySliceInfo

import os

import testlib

from pygr.sqlgraph import SQLiteServerInfo

def main():
    """This function returns argument
    Example:
    >>> main()
    1 sql:1[0:50] gi|171854975|dbj|AB364477.1|[0:50]
    2 sql:2[0:100] -gi|171854975|dbj|AB364477.1|[300:400]
    """

    dna_db.__doc__ = 'DNA database for annotation tutorial'

    worldbase.Bio.pygr.annotationTutorial.dna_db = dna_db

    annodb.__doc__ = 'example annotationdb based on sqlite rows'

    worldbase.Bio.pygr.annotationTutorial.annodb3 = annodb

    worldbase.commit()

    del annodb, slicedb
 
    worldbase.clear_cache()

    annodb3 = worldbase.Bio.pygr.annotationTutorial.annodb3()

    for k in annodb3:
        print k, repr(annodb3[k]), repr(annodb3[k].sequence)


if __name__ == '__main__':
   import doctest
   doctest.testmod()






