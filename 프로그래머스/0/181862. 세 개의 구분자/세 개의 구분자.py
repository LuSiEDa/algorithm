def solution(myStr):
    temp = myStr.replace("a"," ").replace("b", " ").replace("c", " ")
    answer = temp.split()
    return answer if answer else ["EMPTY"]