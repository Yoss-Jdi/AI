G={
    'A' : {
        'B':8 ,
        'C': 6,
        'H': 15,
        'D': 5,
        'G':6
        },

    'B':{
        'A':8,
        'D':10,
        'E':14,
        'F':8,
        'G':10
    },
    'C':{
        'D':5,
        'A':6,
        'H':8
    },
    'D':{
        'A':5,
        'B':10,
        'C':5,
        'E':6
    },
    'E':{
        'B':14,
        'D':6,
        'F':10
    },
    'F':{
        'B':8,
        'E':10,
        'G':12
    },
    'G':{
        'A':6,
        'B':10,
        'H':12,
        'F':12
    },
    'H':{
        'A':15,
        'C':8,
        'G':12
    }
}

def Dijkastra (start,end):
    pi ={
    'A': None,
    'B': None,
    'C': None,
    'D': None,
    'E': None,
    'F': None,
    'G': None,
    'H': None,
    }
    d = {
    'A': float('inf'),
    'B': float('inf'),
    'C': float('inf'),
    'D': float('inf'),
    'E': float('inf'),
    'F': float('inf'),
    'G': float('inf'),
    'H': float('inf')
    }
    d[start]=0 
    visited = set()

    currentNode = start 
    while currentNode != end :
        visited.add(currentNode)
        for child,distance in G[currentNode].items():
            Newdistance = distance+d[currentNode]
            if child not in visited :
                if Newdistance < d[child]:
                    d[child]=Newdistance
                    pi[child]=currentNode
        next = None
        nextDistance = float ('inf')
        for node in G:
            if node not in visited and d[node] < nextDistance:
                nextDistance = d[node]
                next = node
        if next is None:
            break
        currentNode = next
    path = []
    while currentNode is not None:
        path.insert(0, currentNode)
        currentNode = pi[currentNode]

    return path, d[end]

        
d=[]
p,d = Dijkastra('A','H')
print (p,'distance',d)








