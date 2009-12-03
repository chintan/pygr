class MySliceInfo(object):
   def __init__(self, seq_id, start, stop, orientation):
      (self.id, self.start, self.stop, self.orientation) = \
          (seq_id, start, stop, orientation)

from slice_pickle_obj import MySliceInfo

from pygr import seqdb, annotation

from pygr import mapping

seq_id = 'gi|171854975|dbj|AB364477.1|'

slice1 = MySliceInfo(seq_id, 0, 50, +1)

slice2 = MySliceInfo(seq_id, 300, 400, -1)

slice_db = dict(A=slice1, B=slice2)

dna_db = seqdb.SequenceFileDB('data/hbb1_mouse.fa')

slice_db = mapping.Collection(filename='myshelve', mode='c')

slice_db['A'] = slice1

slice_db['B'] = slice2

slice_db.close()

def main():
    """This function returns argument
    Example
    >>> main()
    annotA[0:50] gi|171854975|dbj|AB364477.1|[0:50]
    annotB[0:100] -gi|171854975|dbj|AB364477.1|[300:400]
    """
    slice_db = mapping.Collection(filename='myshelve', mode='r')

    annodb = annotation.AnnotationDB(slice_db, dna_db)

    for k in annodb:
        print repr(annodb[k]), repr(annodb[k].sequence)

if __name__ == '__main__':
   import doctest
   doctest.testmod()






