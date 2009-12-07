
class MySliceInfo(object):
    def __init__(self, seq_id, start, stop, orientation):
        (self.id, self.start, self.stop, self.orientation) = (seq_id, start, stop, orientation)


from pygr import seqdb, annotation, worldbase, mapping, cnestedlist

from slice_pickle_obj import MySliceInfo

import shelve

import os.path

def main():
    """This function returns argument
    Example:
    >>> main()
    baz:A[0:50] gi|171854975|dbj|AB364477.1|[0:50]
    baz:B[0:100] -gi|171854975|dbj|AB364477.1|[300:400]
    baz:A[0:50] gi|171854975|dbj|AB364477.1|[0:50]
    baz:B[0:100] -gi|171854975|dbj|AB364477.1|[300:400]
    gi|171854975|dbj|AB364477.1|[0:444]
    """
    filename = os.path.abspath('data/hbb1_mouse.fa')

    seq_id = 'gi|171854975|dbj|AB364477.1|'

    dna_db = seqdb.SequenceFileDB('data\hbb1_mouse.fa')    

    slicedb = shelve.open('slicedb.db', 'c')

    annodb = annotation.AnnotationDB(slicedb,dna_db)
    
    slice1 = MySliceInfo(seq_id, 0, 50, +1)

    slice2 = MySliceInfo(seq_id, 300, 400, -1)

    annot1 = annodb.new_annotation('A', slice1)

    annot2 = annodb.new_annotation('B', slice2)

    for k in annodb:
        print repr(annodb[k]), repr(annodb[k].sequence)

    dna_db.__doc__ = 'DNA database for annotation tutorial'

    worldbase.Bio.pygr.annotationTutorial.dna_db = dna_db

    annodb.__doc__ = 'example annotationdb based on objects'

    worldbase.Bio.pygr.annotationTutorial.annodb1 = annodb

    worldbase.commit()

    #del annodb, dna_db

    worldbase.clear_cache()

    annodb = worldbase.Bio.pygr.annotationTutorial.annodb1()
    
    for k in annodb:
        print repr(annodb[k]), repr(annodb[k].sequence)

    dna_db = annodb.seqDB

    print repr(dna_db[seq_id])

if __name__ == '__main__':
    import doctest
    doctest.testmod()






