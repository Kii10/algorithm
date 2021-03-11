class UnionFind:
    def __init__(self, n):
        self.par = [-1] * n
        self.siz = [1] * n

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        if self.siz[x] < self.siz[y]:
            x, y = y, x

        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    def size(self, x):
        return self.siz[self.root(x)]


uf = UnionFind(6)
uf.unite(1, 2)
uf.unite(2, 3)
uf.unite(2, 5)
print(uf.issame(1, 4))
print(uf.issame(2, 3))
print(uf.par)
print(uf.root(5))
print(uf.size(3))
