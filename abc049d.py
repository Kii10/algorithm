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


n, k, l = map(int, input().split())
road = UnionFind(n)
line = UnionFind(n)

for i in range(k):
    p, q = map(int, input().split())
    road.unite(p-1, q-1)
for i in range(l):
    r, s = map(int, input().split())
    line.unite(r-1, s-1)

ans = {}
com = [0] * n
for i in range(n):
    x = road.root(i)
    y = line.root(i)
    com[i] = (x, y)
    if not com[i] in ans.keys():
        ans[com[i]] = 1
    else:
        ans[com[i]] += 1

for i in range(n):
    print(ans[com[i]], end=" ")
