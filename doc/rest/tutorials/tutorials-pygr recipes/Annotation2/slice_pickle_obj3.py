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
    foo:C[0:50] gi|171854975|dbj|AB364477.1|[0:50]
    foo:D[0:100] -gi|171854975|dbj|AB364477.1|[300:400]

    """
    annodb = annotation.AnnotationDB({}, dna_db, annotationType='foo:', sliceAttrDict=dict(id='seq_id', start='begin', stop='end', orientation='strand'))

    slice1 = MyFunkySliceInfo(seq_id, 0, 50, +1)
    
    slice2 = MyFunkySliceInfo(seq_id, 300, 400, -1)

    annot1 = annodb.new_annotation('C', slice1)

    annot2 = annodb.new_annotation('D', slice2)

    for k in annodb:
        print repr(annodb[k]), repr(annodb[k].sequence)

if __name__ == '__main__':
   import doctest
   doctest.testmod()






