def solution(n, costs):

    # 부모 테이블 초기화
    p = {}
    for island1, island2, cost in costs:
        p[island1] = island1
        p[island2] = island2

    def find(u):
        if u != p[u]:
            p[u] = find(p[u])
        return p[u]

    def union(u, v):
        root1 = find(u)
        root2 = find(v)
        p[root2] = root1

    # 비용을 기준으로 오름차순 정렬
    costs.sort(key=lambda x: x[2])

    # 최소 신장트리에 포함되는 경로의 비용
    mst_cost = 0

    # 경로 하나씩 크루스칼 알고리즘 수행
    for u, v, cost in costs:
        # 부모노드가 다르면 최소 신장트리에 포함
        if find(u) != find(v):
            union(u, v)
            mst_cost += cost

    return mst_cost
