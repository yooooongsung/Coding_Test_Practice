def dfs(cur_piro, dungeons, cnt, visited):
    max_cnt = cnt

    for i in range(len(dungeons)):
        if dungeons[i][0] <= cur_piro and not visited[i]:
            visited[i] = True
            result = dfs(cur_piro - dungeons[i][1], dungeons, cnt + 1, visited)
            max_cnt = max(max_cnt, result)
            visited[i] = False

    return max_cnt

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    return dfs(k, dungeons, 0, visited)
