

def continuous_sequence(arr):
    best_score = 0
    current_score = 0

    for i in range(len(arr)):
        current_score += arr[i]

        if current_score < 0:
            if current_score - arr[i] > best_score:
                best_score = current_score - arr[i]
            current_score = 0
        else:
            if current_score > best_score:
                best_score = current_score

    print(best_score)

if __name__ == '__main__':
    n = [2, -8, 3, -2, 4, -10, 20, -34]
    continuous_sequence(n)
