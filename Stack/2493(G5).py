'''
https://www.acmicpc.net/problem/2493

< 해설 >
송신탑의 왼쪽 방향으로 가장 가까우면서 더 높은 탑 찾기

실행시간 단축을 위해 스택을 관리 => 불필요한 탑은 삭제 (stack에 검사 중인 송신탑보다 낮거나 같은 탑 발견 시 삭제)
'''

import sys
input = sys.stdin.readline

# 입력
N = int(input())
arr = list(map(int, input().split()))

stack = [arr[0]]
stackI = [1]
top = 0

arrI = [0]*N
# 유효한 탑 중 가까운 순으로 확인 => stack 사용
for i in range(1, N) :
    while True :
        if top == -1 :  # stack empty
            arrI[i] = 0
            break
        
        if stack[top] > arr[i] :    # 가장 가까운 수신탑 발견
            arrI[i] = stackI[top]
            break
        else :  # 송신탑보다 낮음 => stack에서 삭제
            del stack[top]
            del stackI[top]
            top -= 1
    stack.append(arr[i])    # 스택에 추가
    stackI.append(i+1)
    top += 1

for x in arrI : print(x, end = ' ')

''' 코드1 : 시간초과
for i in range(1, N+1) :    # O(N^2)
    for j in range(i-1, -1, -1) :
        if j == 0 :
            print(0, end = ' ')
        if arr[i] < arr[j] :
            print(j, end = ' ')
            break
'''
