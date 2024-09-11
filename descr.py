class Descr:
    coord = None
    lengths = []
    def __init__(self,
                 a:tuple):
        self.coord = a
        self.lengths.append(self.length_of(a[0],a[3]))
        for i in range(0,3):
            self.lengths.append(self.length_of(a[i],a[i+1]))
        self.lengths = sorted(self.lengths)
        pass
    def length_of(self, a, b):
        return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
    def is_equal(self,a):
        for i in range(4):
            if a.lengths[i] != self.lengths[i]:
                return False
        return True
    def is_similar(self, a):
        for i in range(3):
            if self.lengths[i]/a.lengths[i] != self.lengths[i+1]/a.lengths[i+1]:
                return False
        return True