def solution(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1

# 맞추긴 했지만 이게 왜 맞는건지 어리둥절