def solution(X, A):
    mins = [-1] * X
    for i in range(len(A)):
        ind = A[i] - 1
        if mins[ind] == -1 or i < mins[ind]:
            mins[ind] = i
    if -1 in mins:
        return -1
    return max(mins)


x = 5
arr = [1, 3, 1, 4, 2, 3, 5, 4]
expected = 6
print(solution(x, arr))