def solution(myString):
    ch = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    for i in ch:
        myString = myString.replace(i, "l")
    return myString