from collections import defaultdict

# modified BFS
def find_all_parents(G, s):
    Q = [s]
    print(f"Q: {Q}")
    parents = defaultdict(set)
    print(f"Parents: {parents}")
    while len(Q) != 0:
        v = Q[0]
        print(f"v: {v}")
        Q.pop(0)
        print(f"Q: {Q}")
        for w in G.get(v, []):
            parents[w].add(v)
            Q.append(w)
    return parents

# recursive path-finding function (assumes that there exists a path in G from a to b)
def find_all_paths(parents, a, b):
    return [a] if a == b else [y + b for x in list(parents[b]) for y in find_all_paths(parents, a, x)]


#G = {'A':['B','C'], 'B':['D'], 'C':['D', 'F'], 'D':['E', 'F'], 'E':['F']}
#print(find_all_paths(find_all_parents(G, 'A'), 'A', 'F'))

G = {' start ':[' A ',' b '], ' A ':[' b ', ' c ', ' end '],' b ':[' d ', ' end ']}
print(find_all_paths(find_all_parents(G, ' start '), ' start ', ' end '))