def solution(emergency):
    sort_list = sorted(emergency, reverse=True)
    result = []
    for i in emergency:
        ranked = sort_list.index(i)+1
        result.append(ranked)
    return result