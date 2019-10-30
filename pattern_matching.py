

def find_b(pattern):
    for i in range(len(pattern)):
        if pattern[i] == 'b':
            return i
    return -1

def get_max_length(value, pattern, num_a, num_b):
    total_len = len(value)
    total_len -= num_b
    return total_len // num_a

def build_string(a, b, pattern):
    result = ""
    for i in range(len(pattern)):
        if pattern[i] == 'a':
            result += a
        else:
            result += b
    return result


def change_to_a(str):
    result = ""
    for i in range(len(str)):
        if str[i] == 'a':
            result+='b'
        else:
            result+= 'a'
    return result

def pattern_matching(pattern, value):
    if len(pattern) == 1 and len(value) != 0:
        return True
    if pattern[0] == 'b':
        pattern = change_to_a(pattern)
    first_b = find_b(pattern)
    #print(first_b)
    num_a = 0
    num_b = 0

    for i in range(len(pattern)):
        if pattern[i] == 'a':
            num_a += 1
        else:
            num_b += 1

    max_length_a = get_max_length(value,pattern, num_a, num_b)

    for j in range(1, max_length_a + 1):
        b_length = (len(value) - (num_a * j))/num_b

        if b_length % 1 == 0:# and (i * num_a) + (b_length * num_b) == len(value):
            a = value[0:j]

            b = value[(j*first_b):(j*first_b) + int(b_length)]
            print(a)
            print(b)
            test_string = build_string(a, b, pattern)
            print(test_string)

            if test_string == value:
                print('true')
                return True

    return False


if __name__ == '__main__':
   # pattern = "aabab"
   # value = "catcatgocatgo"
    #pattern_matching(pattern, value)
    graph = [[4],[],[4],[4],[0,2,3]]
    for i in range(len(graph)):
        print(len(graph[i]))