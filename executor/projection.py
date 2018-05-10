
from .base import BaseNode

class Projection(BaseNode):
    """
    Read from disk and return a single tuple per next call
    """

    def __init__(self, mapping):
        super().__init__()
        self.mapping = mapping

    def __next__(self):
        # transform to mapping
        result_set = []
        records = next(self.childNode)
        if not records:
            return None
        for record in records:
            result_set.append(self.mapping(record))
        return result_set
