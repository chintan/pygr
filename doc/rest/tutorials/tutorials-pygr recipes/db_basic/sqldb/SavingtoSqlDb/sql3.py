from pygr import sqlgraph
 
from pygr import seqdb, annotation

from pygr import worldbase

def main():
    """This function returns argument.
    Example;
    >>> main()
    <pygr.classutil.TupleORW_annotations object at 0x029DBD70>
    <pygr.classutil.TupleORW_annotations object at 0x029DBB30>
    """
    liteserver = sqlgraph.SQLiteServerInfo('slicedb.sqlite')	

    txInfo = sqlgraph.SQLTable('annotations', serverInfo=liteserver, writeable=True,createTable='CREATE TABLE annotations (k INTEGER PRIMARY KEY, seq_id TEXT, start INT, stop INT, orientation INT);')

    print txInfo.new(k=0,seq_id='gi|171854975|dbj|AB364477.1|',start=0,stop=50,orientation=1)

    print txInfo.new(k=1,seq_id='gi|171854975|dbj|AB364477.1|',start=300,stop=400,orientation= -1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()