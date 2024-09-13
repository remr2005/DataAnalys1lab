class Descr:
    coord = None
    lengths = []
    def __init__(self,
                 a:tuple) -> None:
        # рассчитываю на то что все координаты стоящие рядом связанны между собой
        self.coord = a
        # вычисляю длину всех сторон
        self.lengths.append(self.length_of(a[0],a[3]))
        for i in range(0,3):
            self.lengths.append(self.length_of(a[i],a[i+1]))
        pass
    # вычислние длины по координатам
    def length_of(self, a, b) -> float:
        return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
    # равны ли четырехугольники
    def is_equal(self,a) -> bool:
        # проверяю что все стороны равны
        for i in range(4):
            if a.lengths[i] != self.lengths[i]:
                return False
        return True
    def is_similar(self, a) -> bool:
        a = sorted(a)
        b = sorted(self.lengths)
        for i in range(3):
            if b[i]/a.lengths[i] != b[i+1]/a.lengths[i+1]:
                return False
        return True