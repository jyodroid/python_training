def findNeighbours(wordList, node):
    neighbours = []
    for word in wordList:
        diferences = 0
        if word == node:
            continue
        for i in range(0, len(word)):
            if word[i] != node[i]:
                diferences += 1
                if diferences > 1:
                    break
        if diferences == 1:
            neighbours.append(word)
    return neighbours


def wordLadder(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    if beginWord == endWord:
        return 0

    graph = makeGraph(beginWord, wordList)
    return find_shortest_path_BFS(graph, beginWord, endWord)


def wordLadderDFS(beginWord, endWord, wordList):
    graph = makeGraph(beginWord, wordList)

    return find_shortest_path_DFS(graph, beginWord, endWord, path=[])


def find_shortest_path_DFS(graph, beginWord, endWord, path):

    path = path + [beginWord]

    if beginWord == endWord:
        return path

    if beginWord not in graph:
        return None

    shortest = None

    for node in graph[beginWord]:
        if node not in path:
            newpath = find_shortest_path_DFS(graph, node, endWord, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def find_shortest_path_BFS(graph, beginWord, endWord):

    if (graph[beginWord] or graph[endWord]) == [] or beginWord == endWord:
        return 0

    UNVISITED = 0
    VISITED = 1
    WEIGTH = 1

    auxiliar = {}
    distance = {}
    queue = []

    for node in graph:
        auxiliar[node] = UNVISITED
        distance[node] = None

    auxiliar[beginWord] = VISITED
    distance[beginWord] = 1
    queue.append(beginWord)

    while(queue):
        if endWord in queue:
            return distance[endWord]

        currentNode = queue.pop(0)
        for node in graph[currentNode]:
            if (auxiliar[node] == UNVISITED):
                auxiliar[node] = VISITED
                distance[node] = distance[currentNode] + WEIGTH
                queue.append(node)
    return distance[endWord]


def makeGraph(beginWord, wordList):
    graph = {beginWord: findNeighbours(wordList, beginWord)}
    for word in wordList:
        graph[word] = findNeighbours(wordList, word)
    return graph


def main():
    print wordLadder("hit", "cogi", ["hot", "dot", "dog", "lot", "log", "cog"])
    print wordLadder("hit", "cog", ["hot", "dot", "dol", "lil", "log", "cog"])
    print wordLadder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    print wordLadderDFS("hit", "cog",
                        ["hot", "dot", "dog", "lot", "log", "cog"])
    print findNeighbours(["hot", "dot", "dog", "lot", "log", "cog"], "hot")

    print wordLadder("qa", "sq", ["si", "go", "se", "cm", "so", "ph", "mt",
                     "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm",
                                  "ar", "ci", "ca", "br", "ti", "ba", "to",
                                  "ra", "fa", "yo", "ow", "sn", "ya", "cr",
                                  "po", "fe", "ho", "ma", "re", "or", "rn",
                                  "au", "ur", "rh", "sr", "tc", "lt", "lo",
                                  "as", "fr", "nb", "yb", "if", "pb", "ge",
                                  "th", "pm", "rb", "sh", "co", "ga", "li",
                                  "ha", "hz", "no", "bi", "di", "hi", "qa",
                                  "pi", "os", "uh", "wm", "an", "me", "mo",
                                  "na", "la", "st", "er", "sc", "ne", "mn",
                                  "mi", "am", "ex", "pt", "io", "be", "fm",
                                  "ta", "tb", "ni", "mr", "pa", "he", "lr",
                                  "sq", "ye"])

    print findNeighbours(["abc", "acc", "acb"], "abc")
    print wordLadder("abc", "acb", ["abc", "acc", "acb"])
    print wordLadder("abc", "add", ["abc", "acc", "acb", "add", "abd"])

if __name__ == '__main__':
    main()
