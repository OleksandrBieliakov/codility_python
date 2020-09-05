def solution(S, K):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    ind = days.index(S)
    new_ind = (ind + K) % 7
    return days[new_ind]


print(solution('Wed', 2))
print(solution('Sat', 23))
