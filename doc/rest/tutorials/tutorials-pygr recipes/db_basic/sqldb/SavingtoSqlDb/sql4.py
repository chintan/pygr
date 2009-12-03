from pygr import sqlgraph
 
from pygr import seqdb, annotation

from pygr import worldbase

def main():
    """This function returns argument.
    Example:
    >>> main()
    2
    []
    0
    """
    liteserver = sqlgraph.SQLiteServerInfo('slicedb.sqlite')	

    txInfo = sqlgraph.SQLTable('annotations', serverInfo=liteserver, writeable=True,createTable='CREATE TABLE annotations (k INTEGER PRIMARY KEY, seq_id TEXT, start INT, stop INT, orientation INT);')

    dna_db = seqdb.SequenceFileDB('data/hbb1_mouse.fa')

    annodb = annotation.AnnotationDB(txInfo, dna_db, sliceAttrDict=dict(id='seq_id'))

    print len(txInfo)

    print txInfo.keys()
    
    print len(annodb)

if __name__ == '__main__':
    import doctest
    doctest.testmod()





