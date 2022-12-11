def depth(l):
    if isinstance(l, list):
        if not len(l):
            l.append(0)  #Just to make sure the program doesn't crash when there's nothing
        return 1 + max(depth(item) for item in l)
    else:
        return 0
L = [1,2,3]
print(depth(L))
print(depth([1,[2,[]],[4,5]]))
print(depth([1,[2,[[4,[5]]]]]))
print(depth([1,2,3,[4,[5,[6,7,[8,9]]]]]))
print(depth([1,2,3,[4,[5,[6,7,[8,9,[10,11,[12,[13,14]]]]]]]]))