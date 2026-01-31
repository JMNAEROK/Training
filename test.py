#하노이탑
#1 -> 3 옮기는데 가장 큰 원판을 3으로 옮기면 나머지는 자동
#큰 원판을 옮기는 것의 하위 문제는 ?
#나머지 원판을 임시 구역으로 옮기는 것
#나머지 원판을 임시 구역으로 옮기는 건 2번째로 큰 원판을 임시구역으로 옮기는 것과 같음

def hanoi (N, start, end, temp) :
    if N == 1 :
        print(start, end)
        return
    hanoi (N-1, start, temp, end)
    print(start, end)
    hanoi (N-1, temp, end, start)
    
    
N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 3, 2)