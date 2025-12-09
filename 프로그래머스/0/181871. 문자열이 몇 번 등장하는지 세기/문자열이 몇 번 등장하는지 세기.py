def solution(myString, pat):
        L = len(pat)
        return sum(myString[i:].startswith(pat) for i in range(len(myString)-L+1))