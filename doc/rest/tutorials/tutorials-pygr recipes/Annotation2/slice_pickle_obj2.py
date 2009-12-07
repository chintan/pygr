class MySliceInfo(object):
   def __init__(self, seq_id, start, stop, orientation):
      (self.id, self.start, self.stop, self.orientation) = \
          (seq_id, start, stop, orientation)

class MyFunkySliceInfo(object):
   def __init__(self, seq_id, begin, end, strand):
       (self.seq_id, self.begin, self.end, self.strand) = \
          (seq_id, begin, end, strand)

from pygr import seqdb, annotation, worldbase, mapping, cnestedlist

from slice_pickle_obj import MySliceInfo, MyFunkySliceInfo

seq_id = 'gi|171854975|dbj|AB364477.1|'

dna_db = seqdb.SequenceFileDB('data/hbb1_mouse.fa')

def main():
    """This function returns argument
    Example:
    >>> main()
    foo:A[0:50]
    foo:B[0:100]
    """
    seq_id = 'gi|171854975|dbj|AB364477.1|'

    annodb = annotation.AnnotationDB({}, dna_db, annotationType='foo:')

    slice1 = MySliceInfo(seq_id, 0, 50, +1)
    
    slice2 = MySliceInfo(seq_id, 300, 400, -1)

    annot1 = annodb.new_annotation('A', slice1)

    annot2 = annodb.new_annotation('B', slice2)

    for k in annodb:
        print repr(annodb[k])


if __name__ == '__main__':
   import doctest
   doctest.testmod()






