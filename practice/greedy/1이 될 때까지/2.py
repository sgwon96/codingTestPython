n,k = map(int, input().split())
count = 0

while True:
    # (N == K로 나누어 떨어지는 수가 될 때까지 1씩 빼기)
    target  = (n//k) * k
    result += (n - target)
    
    n = target
    
    if n < k:
        break

     result += 1
     n //= k

     # 마지막으로 남은 수에 대해 1씩 빼기
     result +=( n - 1 )
     print(result)

     # 반복문의 횟수를 줄이는 것이 시간 복잡도를 고려할 때 더 효율적으로 설계가 가능

     