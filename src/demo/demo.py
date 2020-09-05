def solution(A):
    # write your code in Python 3.6
    occured = set()
    for n in A:
        occured.add(n)

    max_occured = max(occured)
    if max_occured < 1:
        return 1

    for i in range(1, max_occured + 2):
        if i not in occured:
            return i

arr = [1,2,3]
arr2 = [-1, -3]
print(solution(arr))
print(solution(arr2))
