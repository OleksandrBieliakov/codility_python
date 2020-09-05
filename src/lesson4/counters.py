def solution(N, A):
    counters = [0] * N
    mx = 0
    for i in A:
        if i == N + 1:
            for j in range(N):
                counters[j] = mx
        else:
            counters[i - 1] += 1
            if counters[i - 1] > mx:
                mx = counters[i - 1]
    return counters


n = 5
arr = [3, 4, 4, 6, 1, 4, 4]
expected = [3, 2, 2, 4, 2]
print(solution(n, arr))
