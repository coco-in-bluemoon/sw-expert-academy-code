from collections import defaultdict
from collections import deque


def construct_tree():
    tree = defaultdict(set)
    node = 1
    height = 1
    while node <= 10000:
        for h in range(height):
            if h < height-1:
                tree[node].add(node+1)
                tree[node+1].add(node)

            tree[node].add(node+height)
            tree[node].add(node+height+1)
            tree[node+height].add(node)
            tree[node+height+1].add(node)

            node += 1
        height += 1

    return tree


def bfs(start, target, tree):
    visited = set()
    counter = 0
    queue = deque([(start, counter)])

    while queue:
        node, counter = queue.popleft()
        if node in visited:
            continue

        if node == target:
            break

        visited.add(node)

        for children in tree[node]:
            if children in visited:
                continue
            queue.append((children, counter+1))

    return counter


def solution(position, treasure, tree):
    counter = bfs(position, treasure, tree)
    return counter


if __name__ == "__main__":
    filename = '이상한 피라미드 탐험.txt'
    inputs = open(f'./D5/inputs/{filename}', 'r')
    outputs = open(f'./D5/outputs/{filename}', 'r')

    T = int(inputs.readline())
    tree = construct_tree()

    for t in range(T):
        position, treasure = map(int, inputs.readline().split())
        answer = int(outputs.readline().split()[1])

        my_answer = solution(position, treasure, tree)
        assert my_answer == answer
