import game
from node import Node


def MiniMax(node, flag):
    if flag:
        return MaxMin(node)
    else:
        return MinMax(node)


def MaxMin(node):
    if node.child == '':
        return static(node)
    else:
        v = -10000000
        for child in node.child:
            try:
                v = max(v, MinMax(child))
                return v
            except TypeError:
                print('error type:', MinMax(child))


def MinMax(node):
    if node.child == '':
        return static(node)
    else:
        v = 10000000
        for child in node.child:
            try:
                v = min(v, MaxMin(child))
                return v
            except TypeError:
                print('error type:', MaxMin(child))


def static(node):
    print('Output:', node.value)
    return game.StaticEstimation(node.value, 'Opening')


def choose_min_or_max(position):
    w_count, b_count = 0, 0
    for loc in position:
        if loc == 'W':
            w_count += 1
        if loc == 'B':
            b_count += 1
    if w_count <= b_count:
        return True
    else:
        return False


def create_tree(position, depth, flag):
    children = []
    if flag:
        pos_w = game.MovesOpening(position)
        if depth > 0:
            for i in range(len(pos_w)):
                child = Node(pos_w[i], create_tree(pos_w[i], depth-1, not flag))
                children.append(child)
        else:
            for i in range(len(pos_w)):
                child = Node(pos_w[i], '')
                children.append(child)
    else:
        pos_b = game.MoveGenerator(position, 'Opening')
        if depth > 0:
            for i in range(len(pos_b)):
                child = Node(pos_b[i], create_tree(pos_b[i], depth-1, not flag))
                children.append(child)
        else:
            for i in range(len(pos_b)):
                child = Node(pos_b[i], '')
                children.append(child)
    return children


if __name__ == '__main__':
    position = []
    fp = open('board1.txt', 'r')
    for ch in fp.read():
        position.append(ch)
    fp.close()

    flag = choose_min_or_max(position)
    depth = 4
    root = Node(position, create_tree(position, depth, flag))
    print(MiniMax(root, flag))
