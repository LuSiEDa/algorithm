def solution(arr, intervals):
    group1 = arr[intervals[0][0]:intervals[0][1]+1]
    group2 = arr[intervals[1][0]:intervals[1][1]+1]
    return group1 + group2