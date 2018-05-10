import csv

from .base import BaseNode

class FileScan(BaseNode):
    """
    Read from disk and return a single tuple per next call
    """

    def __init__(self, table_name, record_type):
        self.record_type = record_type
        table = "data/" + table_name  + ".csv"
        self.fp = open(table, 'r')
        self.reader = csv.reader(self.fp)
        next(self.reader)

    def __next__(self):
        try:
            row = next(self.reader)
            return self.record_type(*row)
        except StopIteration:
            return None


    def __delete__(self):
        self.fp.close()
