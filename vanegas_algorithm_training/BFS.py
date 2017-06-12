def findNeighbours(wordList, node):
    neighbours = []
    for word in wordList:
        diferences = 0
        if word == node:
            continue
        for i in range (0, len(word)):
            if word[i] != node[i]:
                diferences+=1
                if diferences > 1:
                    break
        if diferences == 1:
            neighbours.append(word)
    return neighbours

def wordLadder(beginWord, endWord, wordList):
    graph = makeGraph(beginWord, wordList)

    return find_shortest_path(graph, beginWord, endWord, path =[], visited=[])

def find_shortest_path(graph, beginWord, endWord, path, visited):

    path = path + [beginWord]
    visited = visited + [beginWord]

    if beginWord == endWord:
        return path

    if not graph.has_key(beginWord):
        return None

    shortest = None

    for node in graph[beginWord]:
        if node not in path and node not in visited:
            newpath = find_shortest_path(graph, node, endWord, path, visited)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def makeGraph(beginWord, wordList):
    graph = {beginWord: findNeighbours(wordList, beginWord)}
    for word in wordList:
        graph[word] = findNeighbours(wordList, word)
    return graph


def main():
    print wordLadder("hit", "cogi", ["hot", "dot", "dog", "lot", "log", "cog"])
    print len(wordLadder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print findNeighbours(["hot", "dot", "dog", "lot", "log", "cog"], "hot")

if __name__ == '__main__':
    main()
