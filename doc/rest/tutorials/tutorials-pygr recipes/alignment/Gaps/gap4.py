
 
from pygr import seqdb, annotation

from pygr import cnestedlist

def main():
    """This function returns argument.
    Example:
    >>> main()
    ungapped[0:70] gapped[0:74] 0.946
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

    for (src, dest, edge) in al[ungapped].edges(maxinsert=4):
        print repr(src), repr(dest), '%.3f' % (edge.pIdentity(),)
   
     
if __name__ == "__main__":
    import doctest
    doctest.testmod()
