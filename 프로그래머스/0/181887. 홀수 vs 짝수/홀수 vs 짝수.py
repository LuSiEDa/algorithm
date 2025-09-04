def solution(num_list):
    odd = sum(num_list[0::2])
    even = sum(num_list[1::2])
    if odd > even:
        return odd
    elif odd < even:
        return even
    else:
        return odd