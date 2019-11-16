def one_away(s1, s2):
    if len(s2) > len(s1):
        return one_away(s2, s1)
    if len(s1)> len(s2) +1:
        return False
    if len(s2) == len(s1):
        return same_helper(s1, s2)

    diff = False

    ptr1 = 0
    ptr2 = 0

    while ptr2< len(s2):
        if s1[ptr1] != s2[ptr2]:
            if diff:
                return False
            else:
                diff = True
                ptr1 += 1
        else:
            ptr1+=1
            ptr2+=1

    return True

def same_helper(s1, s2):
    diff = False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if diff:
                return False
            else:
                diff = True

    return True

if __name__ == '__main__':
    print(one_away("pale", "balf"))