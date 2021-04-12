![](https://images.velog.io/images/sgwon1996/post/46c608e5-cdac-4b6e-aee1-7483c824fa2f/unnamed.jpg)

## 파이썬 기초 100제

파이썬 문법을 다시 공부하기 위해 코드업에서 파이썬 기초 100제를 풀었다. 그리고 기초 100제를 풀면서 새롭게 배운 문법들을 정리하고자 한다. 아래 사이트에서 기초 100제를 풀어 볼 수 있다. 파이썬 공부를 시작하고 기초 문법들을 복습하기에 쉽고 좋은 문제들이다.

https://codeup.kr/problemsetsol.php?psid=33

## 파이썬 문법

### 8. 출력하기08

```python
print("print(\"Hello\\nWorld\")")
```
> 파이썬 문법안에 있는 문자를 출력할때는 앞에 \를 붙여주면 된다.

### 15.  정수 2개 입력받아 그대로 출력하기2

```python
arr = list(map(int,input().split()))
for i in arr:
    print(i)
```

> 공백을 기준으로 문자를 입력받은 후 map 함수를 통해 모두 int형으로 만들고 list로 만들어 주었다. 그 후 리스트를 for문을 통해 하나씩 출력했다.

### 19. 연월일 입력받아 순서 바꿔 출력하기

```python
y, m, d = input().split('.') 
print(d, m, y, sep='-')
```

> split 함수를 통해서 . 로  연월일을 구분하여 입력 받고 print()함수에서 sep 속성을 통해 - 로 나눠 출력을 해주었다.

### 22. 연월일 입력받아 나누어 출력하기

```python
s = input()
print(s[0:2], s[2:4], s[4:6], sep=' ')
```

> 문자열을 입력받은 후 문자열 슬라이싱을 활용해 나누어 출력했다. 
[0:2] 는 s[0], s[1] 이렇게 두글자 까지 출력한다.

### 27. 10진 정수 입력받아 16진수로 출력하기

```python
a = int(input())
print("%x"%a)
```
> %x 포맷을 통해 16진수 소문자로 출력 가능하다.
%X 는 대문자로 출력한다.

### 29. 16진수로 입력받아 8진수로 출력

```python
a = int(input(), 16)
print("%o"%a)
```

> int 함수에서 두번째 인자를 넣어주면 그 숫자로 진수를 바꿔준다. print함수에서 %o 포맷을 통해 8진수로 출력 가능하다.

### 30. 영문자 1개 입력받아 10진수로 변환하기

```python
n = ord(input())
print(n)
```
> n = ord(input())  
입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.

### 31. 정수 입력받아 유니코드 문자로 변환하기

```python
c = int(input())
print(chr(c))
```
>print(chr(c))  
c에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다. 

### 38. 정수 2개 입력받아 거듭제곱 계산하기

```python
a,b = map(int,input().split(" "))
print(a**b)
```
> ** 연산자를 이용하면 거듭제곱 연산을 할 수 있다.

### 40. 정수 2개 입력받아 나눈 몫 계산하기

```python
a,b = map(int,input().split(" "))
print(a//b)
print(a%b)
```

>  // 연산자를 이용하면 몫을 구할 수 있다. 
%를 이용하면 나머지를 구할 수 있다.

### 43. 실수 2개 입력받아 나눈 결과 계산하기

```python
a,b = map(float,input().split(" "))
print("%.2f"%(a/b))
```

> %.2f 포맷을 통해 소수점 둘째자리까지 출력해준다.

#### 47. 2의 거듭제곱 배로 곱해 출력하기

```python
a,b = map(int,input().split(" "))
print(a<<b)
```

> <<  시프트 연산은 2를 곱해준다

### 52.정수 입력받아 참 거짓 평가하기(설명)

```python
a = int(input())
print(bool(a))
```
> bool 함수를 이용해 정수값을 참,거짓으로 바꿀 수 있다.

### 56. 참/거짓이 서로 다를 때에만 참 출력하기

```python
a,b = map(int,input().split(" "))
print(bool(a)^bool(b))
```

> ^ 연산자를 통해 xor 연산을 해주었다. 두가지 값이 다를 때 참

### 63. [기초-3항연산] 정수 2개 입력받아 큰 값 출력하기

```python
a,b = map(int,input().split())
print(a if a>b else b)
```

> a if 조건 else b
조건을 만족하면 a 아니면 b

### 64. 정수 3개 입력받아 가장 작은 값 출력하기

```python
numbers = list(map(int,input().split()))
print(min(numbers))
```

> min 함수를 통해 리스트에서 가장 작은값을 구할 수 있다.

### 84. 소리 파일 저장용량 계산하기

```python
h, b, c, s = map(int, input().split())
print('%.1f'% ((h*b*c*s)*(2**-23)), 'MB')
```

> ** 연산자를 통해 2의 23승으로 간편하게 나누어주었다. 
bit를 MB로 바꿀때 간편하게 표현이 가능하다.


### 92. 이상한 출석 번호 부르기 1

```python
cnt = int(input())
nums = list(map(int,input().split()))
d = [ 0 for _ in range(23)]

for num in nums:
    d[num-1] = d[num-1] + 1

for answer in d :
    print(answer,end=" ")

```

> d = [ 0 for _ in range(23)] 
0이 23개 들어있는 리스트로 초기화

### 95. 바둑판에 흰 돌 놓기

```python
d = [[0 for j in range(19)] for i in range(19)] 
cnt = int(input())

for _ in range(cnt):
    x,y = map(int,input().split())
    d[y-1][x-1] = 1

for i in range(19) :
    for j in range(19) :
        print(d[j][i], end=" ")
    print("")

```

> d = [[0 for j in range(19)] for i in range(19)]
0이 19X19 로 들어가 있는 이중리스트 초기화

### 96. 바둑알 십자 뒤집기

```python
d = []
for i in range(19):                                 # 입력
    line = list(map(int,input().split()))
    d.append(line)
```

> 바둑판 입력받기 한줄 씩 리스트로 입력을 받은 후 미리 선언한 리스트에 추가해준다.
