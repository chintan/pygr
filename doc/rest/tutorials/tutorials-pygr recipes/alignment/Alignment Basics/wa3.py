from pygr import sqlgraph
 
from pygr import seqdb, annotation

from pygr import worldbase

from pygr import cnestedlist

def main():
    """This function returns argument.
    Example:
    >>> main()
    0.0068
    """
    simple_al = cnestedlist.NLMSA('hbb', mode='memory', pairwiseMode=True)

    db = seqdb.SequenceFileDB('data/sp_all_hbb')

    mouse = db['HBB1_MOUSE']

    rat = db['HBB1_RAT']

    frog = db['HBB1_XENLA']

    simple_al += mouse

    db = seqdb.SequenceFileDB('data/sp_all_hbb')

    ival = mouse[40:60]

    simple_al[ival] += rat[42:62]

    simple_al[ival] += frog[38:58]

    simple_al.build()
    
    sub_ival = mouse[48:52]

    edge = simple_al[mouse][rat]

    print '%.4f' % (edge.pIdentity(),)


if __name__ == '__main__':
    import doctest
    doctest.testmod()











