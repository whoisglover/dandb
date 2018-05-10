
from .base import BaseNode

class Selection(BaseNode):
    """
    Read from disk and return a single tuple per next call
    """

    def __init__(self, predicate):
        super().__init__()
        self.predicate = predicate

    def __next__(self):
        result_set = []
        while True:
            record = next(self.childNode)
            if not record:
                if(len(result_set)):
                    return result_set
                return None
            if self.predicate(record):
                result_set.append(record)
