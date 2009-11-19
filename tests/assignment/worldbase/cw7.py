
from pygr import worldbase

def main():
    """This function returns the argument.
    Example:
    >>> main()
    Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/leec/projects/pygr/pygr/metabase.py", line 1201, in __call__
    return self._mdb(self._path, *args, **kwargs)
  File "/Users/leec/projects/pygr/pygr/metabase.py", line 647, in __call__
    for objdata,docstr in self.find_resource(resID, download):
  File "/Users/leec/projects/pygr/pygr/metabase.py", line 877, in find_resource
    raise WorldbaseNotFoundError('unable to find %s in WORLDBASEPATH' % resID)
pygr.metabase.WorldbaseNotFoundError: 'unable to find Bio.MSA.UCSC.hg18_multiz44way in WORLDBASEPATH'
    """
    worldbase.update('.')
     
    print msa = worldbase.Bio.MSA.UCSC.hg18_multiz44way()
 
if __name__ == '__main__':
        import doctest
        doctest.testmod()



