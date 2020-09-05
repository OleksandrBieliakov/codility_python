def solution(A, B, K):
    divisible = 0
    for i in range(A, B + 1):
        if i % K == 0:
            divisible += 1
            divisible += (B - i) // K
            break
    return divisible
