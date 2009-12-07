from pygr import sqlgraph
 
from pygr import seqdb, annotation

from pygr import worldbase

from pygr import cnestedlist

def main():
    """This function returns argument.
    Example:
    >>> main()
    HBB1_MOUSE[40:60] aligns to HBB1_RAT[42:62]
    Identity across alignment: 0.15
    --
    HBB1_MOUSE[40:60] aligns to HBB1_XENLA[38:58]
    Identity across alignment: 0.05
    --
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

    for src, dest, edge in simple_al[mouse].edges():
      print repr(src), 'aligns to', repr(dest)
      print 'Identity across alignment:', edge.pIdentity()
      print '--'


if __name__ == '__main__':
    import doctest
    doctest.testmod()











