def no_dups(s):
    # Your code here
    num = 0
    dic = {}
    x = s.split()
    for word in x:
        if word in dic:
            continue
        else:
            num += 1
            dic[word] = num
    return ' '.join(dic.keys())
    # print(dic)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
