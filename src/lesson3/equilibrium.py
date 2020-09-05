def solution(A):
    size = len(A)
    if size == 0:
        return -1
    left_sum = 0
    right_sum = sum(A) - A[0]

    for i in range(size):
        if left_sum == right_sum:
            #print(left_sum, right_sum, "i =", i)
            return i
        left_sum += A[i]
        if i + 1 < size:
            right_sum -= A[i + 1]
        else:
            right_sum = 0
    return -1


arr = [-1, 3, -4, 5, 1, -6, 2, 1]
print(solution(arr))
arr = []
print(solution(arr))
arr = [1, -1, 100]
print(solution(arr))
