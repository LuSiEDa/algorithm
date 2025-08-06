def solution(my_string, letter):
    answer = ''
    return ''.join(st for st in my_string if st not in letter)