class MySliceInfo(object):
   def __init__(self, seq_id, start, stop, orientation):
      (self.id, self.start, self.stop, self.orientation) = (seq_id, start, stop, orientation)

class MyFunkySliceInfo(object):
   def __init__(self, seq_id, begin, end, strand):
       (self.seq_id, self.begin, self.end, self.strand) = (seq_id, begin, end, strand)

from pygr import seqdb, annotation, worldbase, mapping, cnestedlist

from slice_pickle_obj import MySliceInfo, MyFunkySliceInfo

dna_db = seqdb.SequenceFileDB('data\hbb1_mouse.fa')

seq_id = 'gi|171854975|dbj|AB364477.1|'

def main():
    """This function returns argument
    Example:
    >>> main()
    baz:slice1[0:50] gi|171854975|dbj|AB364477.1|[0:50]
    baz:slice2[0:100] -gi|171854975|dbj|AB364477.1|[300:400]
    """
    slicedb = { 'slice1' : MySliceInfo(seq_id, 0, 50, +1), 'slice2' : MySliceInfo(seq_id, 300, 400, -1) }

    annodb = annotation.AnnotationDB(slicedb, dna_db, annotationType='baz:')

    for k in annodb:
        print repr(annodb[k]), repr(annodb[k].sequence)

if __name__ == '__main__':
   import doctest
   doctest.testmod()






