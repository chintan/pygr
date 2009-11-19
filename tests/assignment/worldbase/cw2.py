

from pygr import worldbase

def main():
    """This function returns the argument.
    Example:
    >>> main()
    ['0root', 'Bio', 'Test', '__doc__']
    ['MSA', 'Seq']
    ['Genome']
    ['ANOCA', 'ANOGA', 'APIME', 'BOVIN', 'BRAFL', 'CAEBR', 'CAEEL', 'CAEJA', 'CAEPB', 'CAERE', 'CALJA', 'CANFA', 'CAVPO', 'CHICK', 'CHOHO', 'CIOIN', 'DANRE', 'DASNO', 'DIPOR', 'DROAN', 'DROER', 'DROGR', 'DROME', 'DROMO', 'DROPE', 'DROPS', 'DROSE', 'DROSI', 'DROVI', 'DROWI', 'DROYA', 'ECHTE', 'ERIEU', 'FELCA', 'FUGRU', 'GASAC', 'GORGO', 'HORSE', 'HUMAN', 'LAMPA', 'LOXAF', 'MACMU', 'MICMU', 'MONDO', 'MOUSE', 'MYOLU', 'OCHPR', 'ORNAN', 'ORYLA', 'OTOGA', 'PANTR', 'PETMA', 'PONAB', 'PONPA', 'PRIPA', 'PROCA', 'PTEVA', 'RABIT', 'RAT', 'SORAR', 'SPETR', 'STRPU', 'TAEGU', 'TARSY', 'TETNG', 'TRICA', 'TUPGB', 'TURTR', 'XENTR', 'YEAST']     
    ['mm5', 'mm6', 'mm7', 'mm8', 'mm9']
    {'Bio.Seq.Genome.MOUSE.mm9': {'pickle_size': 186, 'creation_time': <DateTime '20090903T13:07:57' at 7b30f8>, 'user': 'deepreds', '__doc__': 'Mouse Genome (July 2007)'}, 'Bio.Seq.Genome.MOUSE.mm8': {'pickle_size': 186, 'creation_time': <DateTime '20090903T13:07:57' at 7b30d0>, 'user': 'deepreds', '__doc__': 'Mouse Genome (March 2006)'}, 'Bio.Seq.Genome.MOUSE.mm5': {'pickle_size': 186, 'creation_time': <DateTime '20090903T13:07:57' at 7b3120>, 'user': 'deepreds', '__doc__': 'Mouse Genome (May 2004)'}, 'Bio.Seq.Genome.MOUSE.mm7': {'pickle_size': 186, 'creation_time': <DateTime '20090903T13:07:57' at 7b3198>, 'user': 'deepreds', '__doc__': 'Mouse Genome (August 2005)'}, 'Bio.Seq.Genome.MOUSE.mm6': {'pickle_size': 186, 'creation_time': <DateTime '20090903T13:07:57' at 7b3210>, 'user': 'deepreds', '__doc__': 'Mouse Genome (March 2005)'}}
    """
    from pygr import worldbase

    print dir(worldbase)

    print dir(worldbase.Bio)

    print dir(worldbase.Bio.Seq)

    print dir(worldbase.Bio.Seq.Genome)

    print dir(worldbase.Bio.Seq.Genome.MOUSE)

    print worldbase.dir('Bio.Seq.Genome.MOUSE', asDict=True)

if __name__ == '__main__':
        import doctest
        doctest.testmod()



