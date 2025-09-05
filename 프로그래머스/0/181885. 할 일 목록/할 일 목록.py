def solution(todo_list, finished):
    updat = []
    for i in range(len(todo_list)):
        if finished[i] == False:
            updat.append(todo_list[i])
    return updat
