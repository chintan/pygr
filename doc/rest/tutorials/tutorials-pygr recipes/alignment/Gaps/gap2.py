
 
from pygr import seqdb, annotation

from pygr import cnestedlist

def main():
    """This function returns argument.
    Example:
    >>> main()
    gapped[0:40] ungapped[0:40] 1.00
    gapped[44:74] ungapped[40:70] 1.00
    ungapped[0:40] gapped[0:40] 1.00
    ungapped[40:70] gapped[44:74] 1.00 
    """
    simple_al = cnestedlist.NLMSA('hbb', mode='memory', pairwiseMode=True)

    db = seqdb.SequenceFileDB('data/gapping.fa')
   
    ungapped = db['ungapped']
	
    gapped = db['gapped']

    al = cnestedlist.NLMSA('hbb', mode='memory', pairwiseMode=True)
    
    al += gapped
    
    first_ival = gapped[:40]
    
    second_ival = gapped[44:]

    al[first_ival] += ungapped[:40]
 
    al[second_ival] += ungapped[40:]
 
    al.build()

    for (src, dest, edge) in al[gapped].edges():
        print repr(src), repr(dest), '%.2f' % (edge.pIdentity(),)

    for (src, dest, edge) in al[ungapped].edges():
        print repr(src), repr(dest), '%.2f' % (edge.pIdentity(),)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
