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
    [sql:1[0:50], -sql:2[0:100]]
    [sql:1[0:50]]
    """
    annodb = worldbase.Bio.pygr.annotationTutorial.annodb3()

    al = cnestedlist.NLMSA('foo', 'memory', pairwiseMode=True)

    for k in annodb:
        al.addAnnotation(annodb[k])

    al.build()

    dna_db = worldbase.Bio.pygr.annotationTutorial.dna_db()

    seq_id = 'gi|171854975|dbj|AB364477.1|'

    seq = dna_db[seq_id]

    print al[seq].keys()

    print al[seq[:100]].keys()

if __name__ == '__main__':
   import doctest
   doctest.testmod()






