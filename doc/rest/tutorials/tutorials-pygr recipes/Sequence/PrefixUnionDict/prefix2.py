
from pygr import seqdb

from pygr import worldbase

def main():    
    """This function returns argument.
    Example:
    >>> main()    
    hg17.chr1
    chr1
    mm8.chr5
    """    
    mm8 = worldbase.Bio.Seq.Genome.MOUSE.mm8()
    
    rn4 = worldbase.Bio.Seq.Genome.RAT.rn4()
        
    hg17 = worldbase.Bio.Seq.Genome.HUMAN.hg17()
    
    pud = seqdb.PrefixUnionDict(dict(hg17=hg17, mm8=mm8, rn4=rn4))
    
    idDict = ~pud

    chr1 = pud['hg17.chr1']
 
    print idDict[chr1]
  
    print chr1.id
 
    mouse_chr5 = pud['mm8.chr5']
    
    print idDict[mouse_chr5]

if __name__ == "__main__":
    import doctest
    doctest.testmod()