n = int(input())

tree = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(start, tree, parent):
    for child in tree[start]:
        if parent[child] == 0: # 아직 방문하지 않은 노드인 경우
            parent[child] = start # 현재 노드를 자식 노드의 부모로 설정
            dfs(child, tree, parent)

# 루트노드에서 시작해 dfs 실행
dfs(1, tree, parent)

for i in range(2, n + 1):
    print(parent[i])