class disJointSet:
    def __init__(self,n):
        self.rank=[1]*n
        self.parent = [i for i in range(n)]

    def find(self,x):
        if(self.parent[x]!=x):
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        xset=self.find(x)
        yset=self.find(y)

        if xset == yset:
            return 

        if self.rank[xset]<self.rank[yset]:
            self.parent[xset]=yset

        elif self.rank[yset]<self.rank[xset]:
            self.parent[yset]=xset

        else:
            self.parent[yset]=xset
            self.rank[xset]=self.rank[xset]+1

dSet = disJointSet(5)
dSet.union(0,1)
dSet.union(1,2)
dSet.union(3,4)

if dSet.find(0) == dSet.find(2):
    print("Yes")
else:
    print("No")

if dSet.find(0) == dSet.find(3):
    print("Yes")
else:
    print("No")

