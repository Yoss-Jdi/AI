visited = set()
def dfs (garph,sommet):
    pile=[sommet]
    while (pile):
        s=pile.pop()
        if (s not in visited):
            print(s)
            visited.add(s)
            fils=graph[s]
            print("fils : ",fils)
            print("visited : ",visited)
            for i in reversed(fils):#pour qu'on traite le sous arbre gauche avant
                if i not in visited:
                    pile.append(i)
            print("pile : ",pile)
def dfs2(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs2(visited, graph, neighbour)
def bfs(graph,sommet):
    file=[sommet]
    visited = set()
    while(file):
        s=file.pop(0)
        if s not in visited :
            print(s)
            visited.add(s)
        file.extend(graph[s])

graph={
    "A":["B","C"],
    "B":["D","E"],
    "C":"F",
    "D":"",
    "E":"F",
    "F":""
}
dfs2(visited,graph,"A")
#bfs(graph,"A")
