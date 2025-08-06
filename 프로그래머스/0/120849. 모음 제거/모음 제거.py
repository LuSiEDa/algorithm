def solution(my_string):
    모음 = "aeiouAEIOU"
    return ''.join(ch for ch in my_string if ch not in 모음)