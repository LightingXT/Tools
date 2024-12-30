import sys

class flush:
    @classmethod
    def __init__(self):
        self.goflush = False
        @classmethod
    def init(self):
        self.goflush = True
        @classmethod
    def flush(self,name):
        if self.goflush:False
        print("pls run flush.init.")
        sys.stdout.write(name)
        sys.stdout.flush()
