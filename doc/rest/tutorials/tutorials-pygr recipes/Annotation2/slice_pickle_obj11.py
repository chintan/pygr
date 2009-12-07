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
    1 gi|171854975|dbj|AB364477.1| 0
    1 sql:1[0:50] gi|171854975|dbj|AB364477.1|[0:50]
    2 sql:2[0:100] -gi|171854975|dbj|AB364477.1|[300:400]

    """
    dna_db = seqdb.SequenceFileDB('data\hbb1_mouse.fa')

    seq_id = 'gi|171854975|dbj|AB364477.1|'
    
    sqlite = sqlgraph.import_sqlite()

    db = sqlite.connect('slicedb.sqlite')
    
    c = db.cursor()

    _ = c.execute('DROP TABLE IF EXISTS annotations;')
    _ = c.execute('CREATE TABLE annotations (k INTEGER PRIMARY KEY, seq_id TEXT, start INT, stop INT, orientation INT);')

    seq_id = 'gi|171854975|dbj|AB364477.1|'

    _ = c.execute("INSERT INTO annotations (seq_id, start, stop, orientation) VALUES (?, ?, ?, ?)", (seq_id, 0, 50, +1))

    _ = c.execute("INSERT INTO annotations (seq_id, start, stop, orientation) VALUES (?, ?, ?, ?)", (seq_id, 300, 400, -1))

    db.commit()

    dna_db = seqdb.SequenceFileDB('data/hbb1_mouse.fa')

    slicedb = sqlgraph.SQLTable('annotations', serverInfo=SQLiteServerInfo('slicedb.sqlite'))    

    print slicedb[1].id, slicedb[1].seq_id, slicedb[1].start

    annodb = annotation.AnnotationDB(slicedb, dna_db, annotationType='sql:', sliceAttrDict=dict(id='seq_id'))

    for k in annodb:
        print k, repr(annodb[k]), repr(annodb[k].sequence)


if __name__ == '__main__':
   import doctest
   doctest.testmod()






