def solution(string, markers):
    f = 1
    temp = ""
    for i in string:
        if i in markers:
            f = 0
        elif i == "\n":
            f = 1
            if len(temp) > 1 and temp[-1] == " ":
                temp = temp[:-1]
        if f == 1:
            temp += i

    return temp.rstrip(" ")

