from pygr import sqlgraph
 
from pygr import seqdb, annotation

from pygr import worldbase

def main():
    """This function returns argument.
    Example:
    >>> main()
    50
    gi|171854975|dbj|AB364477.1|[0:50]
    gi|171854975|dbj|AB364477.1|[300:400]
    """
    liteserver = sqlgraph.SQLiteServerInfo('slicedb.sqlite')	

    txInfo = sqlgraph.SQLTable('annotations', serverInfo=liteserver, writeable=True,createTable='CREATE TABLE annotations (k INTEGER PRIMARY KEY, seq_id TEXT, start INT, stop INT, orientation INT);')

    dna_db = seqdb.SequenceFileDB('data/hbb1_mouse.fa')

    annodb = annotation.AnnotationDB(txInfo, dna_db, sliceAttrDict=dict(id='seq_id'))

    a = annodb[0]

    print len(a)

    print a.sequence

    a = annodb[1]
    
    print a.sequence

# Once you are done using >>> liteserver.close()


if __name__ == '__main__':
    import doctest
    doctest.testmod()





