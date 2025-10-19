def solution(str1, str2):
    strlist = ""
    for i, j in zip(str1, str2):
        strlist += i + j
    return strlist
