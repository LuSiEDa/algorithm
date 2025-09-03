def solution(strArr):
    lis =[]
    for i in strArr:
        if "ad" not in i:
            lis.append(i)
    return lis