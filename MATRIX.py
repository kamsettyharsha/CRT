class GraphMatrix:
    def __init__(self,size=None,Adj=None):
        if Adj is not None:
            self.Adj=Adj
            self.size=len(Adj)
        else:
            self.size=size
            self.Adj=[[0 for _ in range(size)] for _ in range(size)]
    def add_edge(self,u, v):
        if u < self.size and v < self.size:
            self.Adj[u][v]=1
            self.Adj[v][u]=1
    def display(self):
        print("Adajecnt Matrix")  
        for row in self.Adj:
            print(" ".join(map(str, row))) 
Matrix = [
[0,1,1,0,0,0,0],
[1,0,0,1,0,0,0],
[1,0,0,1,0,0,0],
[0,1,1,0,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,0,1],
[0,0,0,0,0,1,0],
]   
g=GraphMatrix(Adj=Adj)
g.display()






















