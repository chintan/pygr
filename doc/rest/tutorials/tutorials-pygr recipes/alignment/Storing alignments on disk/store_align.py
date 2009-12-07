 
from pygr import seqdb, annotation

from pygr import cnestedlist

def main():
    """This function returns argument.
    Example:
    >>> main()
    [HBB1_RAT[42:62], HBB1_XENLA[38:58]]
    [HBB1_RAT[42:62], HBB1_XENLA[38:58]] 
    """
    simple_al = cnestedlist.NLMSA('hbb', mode='memory', pairwiseMode=True)

    db = seqdb.SequenceFileDB('data/sp_all_hbb')
   
    mouse = db['HBB1_MOUSE']
  
    rat = db['HBB1_RAT']

    frog = db['HBB1_XENLA']

    simple_al += mouse     

    ival = mouse[40:60]
   
    simple_al[ival] += rat[42:62]

    simple_al[ival] += frog[38:58]

    simple_al.build()

    del simple_al

    seqDict = seqdb.PrefixUnionDict({ 'sp_all_hbb': db })

    loaded_al = cnestedlist.NLMSA('tempdir/hbb_mouse.fa', seqDict=seqDict)

    print loaded_al[ival].keys()

    loaded_al = cnestedlist.NLMSA('data/hbb')
    
    seqDict = loaded_al.seqDict

    ival = seqDict['sp_all_hbb.HBB1_MOUSE']

    loaded_al[ival].keys() 
   

if __name__ == "__main__":
    import doctest
    doctest.testmod()
