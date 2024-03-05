
def solution(N):
    num_letters = 26
    num_times = (N + num_letters - 1) // num_letters

    letters = [''] * num_letters

    for i in range(num_letters):
        letters[i] = chr(i + ord('a')) * num_times

    return ''.join(letters)[:N]