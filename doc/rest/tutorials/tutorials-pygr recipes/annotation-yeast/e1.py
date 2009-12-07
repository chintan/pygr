
from pygr import worldbase, annotation, mapping, seqdb

yeast = seqdb.BlastDB('sacCer1')


class YeastGene:

    def __init__(self, name, seq, start, stop, strand):
              
        self.name = name

        self.id = id

        if strand == -1:
            self.start = -stop
            self.stop = -start
                
        else:
            self.start = start
            self.stop = stop

        self.strand = strand

gene_annots = {}

for line in open('sgdGene.txt'):
    info = line.split()

    name = info[0]

    seq = info[1]
  
    if info[2] == '+':
        strand = +1
    
    else:
        strand = -1
        
    start = int(info[3])
    
    stop = int(info[4])
                    
    span = YeastGene(name, seq, strand, start, stop)  
   
    gene_annots[name] = span

# We can now retrieve YeastGene objects by their name; for example,

def main():
    """This function returns argument
    Example:
    >>> main()
    YAL062W 1 31567
    """
    gene_info = gene_annots['YAL062W']
 
    print gene_info.name, gene_info.start, gene_info.stop
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()


