import sys

class Node:
    content = None
    parent = None
    children = None
    pos = 0

    def __init__(self, content, parent, children):
        self.content = content
        self.parent = parent
        if children is not None:
            self.children = children
        else:
            self.children = []
    def show(self, buf = sys.stdout,offset=0):
        lead = ' ' * offset
        buf.write(lead + self.content+ '\n')

        for child in self.children:
            child.show(
                buf,
                offset=offset + 2)

def LoadTree(filename=None):
    #filename = 'D:/graphs.txt'
    reader = open(filename, 'r')

    nodes = {}

    for line in reader:
        line = line.replace('\n', '')
        words = line.split('-')
        if words[0] not in nodes.keys():
            nodes[words[0]] = Node(words[0],None, None)
        if words[1] not in nodes.keys():
            nodes[words[1]] = Node(words[1],None, None)
        parent = nodes[words[0]]
        child = nodes[words[1]]
        parent.children.append(child)

    return nodes['root']

def LoadTokenMap(tokfile=None):
    reader = open(tokfile, 'r')
    tokenMap ={}

    for line in reader:
        line = line.replace('\n', '')
        words = line.split('-')
        for word in words:
            if word not in tokenMap.keys():
                tokenMap[word] = len(tokenMap)

    return tokenMap