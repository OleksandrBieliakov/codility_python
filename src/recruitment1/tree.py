class Tree(object):
    x = 0
    l = None
    r = None

    def __init__(self, val, left, right):
        self.x = val
        self.l = left
        self.r = right


def solution(T):
    if T is None:
        return 0
    return count_visible_children(T) + 1


def count_visible_children(T):
    sum = 0
    if T.l is not None:
        if T.l.x >= T.x:
            sum += 1
        else:
            T.l.x = T.x
        sum += count_visible_children(T.l)
    if T.r is not None:
        if T.r.x >= T.x:
            sum += 1
        else:
            T.r.x = T.x
        sum += count_visible_children(T.r)
    return sum


tree1 = Tree(5, Tree(3, Tree(20, None, None), Tree(21, None, None)), Tree(10, Tree(1, None, None), None))
tree2 = Tree(8, Tree(2, Tree(8, None, None), Tree(7, None, None)), Tree(6, None, None))
print(solution(tree1))
print(solution(tree2))
