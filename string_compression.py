

def string_compression(s):
    if len(s)<2:
        return s

    prev = ""
    current = ""
    count = 0
    result = ""

    for i in range(len(s)):
        if i == 0:
            prev = s[i]
            count += 1
        elif i == len(s)-1:
            if prev != s[i]:
                if count > 1:
                    result += prev
                    result += str(count)
                    result += s[i]
                else:
                    result += prev
                    result += s[i]
            else:
                count += 1
                result += prev
                result += str(count)
        else:
            if prev == s[i]:
                count += 1
            else:
                if count > 1:
                    result += prev
                    result += str(count)
                    prev = s[i]
                    count = 1
                else:
                    result += prev
                    prev = s[i]
                    count = 1
    return result






if __name__ == '__main__':
    print(string_compression("aaalccf"))