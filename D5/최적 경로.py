from collections import deque
import math


def calculate_distance(src, dst):
    dist = abs(dst[0] - src[0]) + abs(dst[1] - src[1])
    return dist


def dfs(source, target, customers, distance, answer):
    if distance > answer:
        return answer

    if not customers:
        d = distance + calculate_distance(source, target)
        return min(d, answer)

    size = len(customers)
    for _ in range(size):
        customer = customers.popleft()
        d = distance + calculate_distance(source, customer)
        temp = dfs(customer, target, customers, d, answer)
        answer = min(answer, temp)
        customers.append(customer)

    return answer


def solution(company, home, customers):
    customers = deque(customers)
    answer = dfs(company, home, customers, 0, math.inf)
    return answer


if __name__ == "__main__":
    filename = '최적 경로.txt'
    inputs = open(f'./D5/inputs/{filename}', 'r')
    outputs = open(f'./D5/outputs/{filename}', 'r')

    T = int(inputs.readline())
    for t in range(1, T+1):
        n = int(inputs.readline())
        line = list(map(int, inputs.readline().split()))

        company = (line[0], line[1])
        home = (line[2], line[3])
        customers = list()

        for x, y in zip(line[4::2], line[5::2]):
            customers.append((x, y))

        my_answer = solution(company, home, customers)

        answer = outputs.readline().strip()
        assert f'#{t} {my_answer}' == answer
