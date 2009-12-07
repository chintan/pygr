
from pygr import seqdb

from pygr import blast

from pygr import cnestedlist

from pygr import annotation

from pygr import translationDB

def main():
    """This function returns argument
    Example:
    >>> main()
    MVHLTDAEKA
    WCT*LMLRRL
    LVVLVSQGSG
    """

    dna_db = seqdb.SequenceFileDB('data/hbb1_mouse.fa')

    translation_db = translationDB.get_translation_db(dna_db)

    frame0 = translation_db.annodb[dna_seq.id + ':-0'] 
  
    print str(frame0[:10]

    frame1 = translation_db.annodb[dna_seq.id + ':-0']

    print str(frame1[:10])

    negframe0 = translation_db.annodb[dna_seq.id + ':-0']

    print str(negframe0[:10])


if __name__ == '__main__':
    import doctest
    doctest.testmod()










