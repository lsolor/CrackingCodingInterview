def longest_word(arr):
    result = ""
    arr.sort(key = lambda s: len(s))
    alpha = {}

    for i in arr:
        if i[0] in alpha:
            alpha[i[0]].append(i)
        else:
            alpha[i[0]]= [i]

    for j in range(len(arr)-1, -1, -1):
        word = arr[j]
        first_letter = alpha[word[0]]

        for x in first_letter:
            if x != word:
                if x == word[:len(x)]:
                    y = word[len(x):]
                    if y in arr:
                        return word


    return "nothing"




if __name__ == '__main__':
    arr = ['cat', 'bananas', 'dog', 'catbananas','nana', 'walk', 'walker', 'dogwalker']
    print(longest_word(arr))