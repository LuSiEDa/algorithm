def solution(array):
    큰수 = max(array)
    인덱스 = array.index(큰수)
    return [큰수, 인덱스]