
from pygr import worldbase

def main():
    """This function returns the argument.
    Example:
    >>> main()
    ['Bio.Seq.Genome.HUMAN.hg17', 'Bio.Seq.Genome.HUMAN.hg18', 'Bio.Seq.Genome.HUMAN.hg19']
    """
    print worldbase.dir('Bio.Seq.Genome.HUMAN')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
