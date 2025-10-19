def solution(age):
    alpha = ["a","b","c","d","e","f","g","h","i","j"]
    nlist = []
    for n in str(age):
        nlist.append(alpha[int(n)])
    return "".join(nlist)