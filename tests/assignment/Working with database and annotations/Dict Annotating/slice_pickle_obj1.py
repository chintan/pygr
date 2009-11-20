
class MySliceInfo(object):
   def __init__(self, seq_id, start, stop, orientation):
      (self.id, self.start, self.stop, self.orientation) = \
          (seq_id, start, stop, orientation)

from slice_pickle_obj import MySliceInfo

from pygr import seqdb, annotation

from pygr import mapping

def main():
    """This function returns argument
    Example:
    >>> main()
    ['A', 'B']
    50
    gi|171854975|dbj|AB364477.1|[0:50] ATGGTGCACCTGACTGATGCTGAGAAGGCTGCTGTCTCTGGCCTGTGGGG

    """
    seq_id = 'gi|171854975|dbj|AB364477.1|'

    slice1 = MySliceInfo(seq_id, 0, 50, +1)

    slice2 = MySliceInfo(seq_id, 300, 400, -1)

    slice_db = dict(A=slice1, B=slice2)

    dna_db = seqdb.SequenceFileDB('data/hbb1_mouse.fa')

    annodb = annotation.AnnotationDB(slice_db, dna_db)

    print annodb.keys()

    a = annodb['A']

    print len(a)

    s = a.sequence
 
    print repr(s), str(s)


if __name__ == '__main__':
   import doctest
   doctest.testmod()






