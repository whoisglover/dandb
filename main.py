
import sys

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

from executor.filescan import FileScan
from executor.selection import Selection
from executor.projection import Projection


# dummy data
# select name from users age > 5
#schema id, name, tag
data = ["1, danny, student", "2, ed, student"]

from collections import namedtuple

# from access.schema import Schema, Int32, Char, Float32

MovieRecord = namedtuple('MovieRecord', ('id', 'name', 'genres'))
RatingRecord = namedtuple('RatingRecord',
                          ('user_id', 'movie_id', 'rating', 'timestamp'))


 # plan: an array of node types and optional predicates
  # ie:
  # [
  #   [Projection, predicate],
  #   [Selection, predicate],
  #   [Scan, filename]
  # ]

#initializaiton method should startup each node and give them the data they need i.e. column names ect



def Main():
    newNamedTuple = namedtuple('newThing', ['name'])
    queryPlan = (
        (Projection, (lambda r: newNamedTuple(r.name),)),
        (Selection, (lambda r: r.id < '0',)),
        (FileScan, ('movies', MovieRecord))
    )

    priorNode = None
    root = None
    for klass, args in queryPlan:
        node = klass(*args)
        if not root:
            root = node
        if priorNode:
            priorNode.childNode = node
        priorNode = node
    result = (next(root))
    print(result)

Main()
