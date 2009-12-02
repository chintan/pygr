
from pygr import worldbase

def main():
    """This function returns the argument.
    Example:
    >>> main()
    17
    "<BlastDB'/Users/leec/projects/pygr/tests/sacCer1'>"
    """
     worldbase.clear_cache()

     yeast = worldbase.Bio.Seq.Genome.YEAST.sacCer1(download=True)

     print len(yeast)
 
     print repr(yeast)
 
if __name__ == '__main__':
        import doctest
        doctest.testmod()



