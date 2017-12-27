def main(vertex, data, root):
    i = 0
    j = 0
    #None = null
    res=[None]*len(vertex)
    X = [1000000000]*len(vertex)
    Y=[0]*len(vertex)
    for i in range(len(Y)):
        Y[i] = vertex[i]

    X[root] = 0
    sort(Y, X)    

    while len(Y) > 0:
        i = extractMin(Y)    
        Adj = adj(data, i)
        for j in Adj:
            weight = w(data, i, j)    
            if Y.count(j)>0 and weight < X[j]:
                res[j] = i
                X[j] = weight
                sort(Y, X)    
    return res

def w(adj, x, y):
    return adj[x][y]


def adj(adj, x):
    vl = []
    for i in range(len(adj)):
        if data[x][i] > 0 and i != x:
            vl.insert(0,i)
    return vl

def sort(Q, K):
    for i in range(len(Q)):
        for j in range(len(Q)):
            if K[Q[i]] < K[Q[j]]:
                s = Q[i]
                Q[i] = Q[j]
                Q[j] = s

def extractMin(Q):
    q = Q[0]
    Q.remove(Q[0])
    return q

data = [ [0,  7,  98,  3,  9],
         [2,  4,  15,  0,  3],
         [0,  11,  99,  1,  7],
         [1,  3,  2,  0,  1],
         [0,  1,  8,  1,  0]]
vertices = [ 0, 1, 2, 3, 4]

res = main(vertices, data, 0)
print (res)


