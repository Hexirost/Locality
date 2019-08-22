class Node:
    
    def __init__(self, data, cacheNodes = "", refNodes = ""):
        self.data           = data
        self.cacheNodes     = cacheNodes
        self.refNodes       = refNodes
    
    def __repr__(self):
        return self.data

    def __str__(self):
        return self.data  +  self.cacheNodes + self.refNodes

        





