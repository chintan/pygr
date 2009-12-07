
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

    gene_info = gene_annots['YAL062W']
 
    annot_db = seqdb.AnnotationDB(gene_annots, yeast)
   
    annot = annot_db['YAL062W']

    first_codon = annot[:3]

    
annot_map = cnestedlist.NLMSA('genes', mode='memory', use_virtual_lpo=True)

def main():
    """This function returns argument
    Example:
    >>> main()
    1
    YAL062W
    """

    for v in annot_db.values():
        annot_map.addAnnotation(v)
        annot_map.build()

    query_sequence = yeast['chr1'][31567:31570]

    annotations = annot_map[query_sequence]
   
    print len(annotations)

    annotation = annotations.keys()[0]
   
    print annotation.name



if __name__ == '__main__':
    import doctest
    doctest.testmod()


