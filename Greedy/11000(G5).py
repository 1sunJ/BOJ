'''
https://www.acmicpc.net/problem/11000

< 문제 >
수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 
김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 
참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
수강신청 대충한 게 찔리면, 선생님을 도와드리자!

< 해설 >
강의실 roomArr에는 해당 수업의 끝나는 시간을 넣고, 넣을 때에는 시작시간으로 비교해가며 수업arr for문 돌리기
 *실행시간 줄이는 방법 :
1. arr 시작시간 기준 정렬
2. roomArr 최소힙
 => O(N*log(len(roomArr)))  (heappush에서 log(size(tree))만큼의 실행 발생)

'''

import heapq
import sys
input = sys.stdin.readline

# 입력
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 코드 3 : 통과 / arr 정렬, roomArr 최소힙
arr.sort(key = lambda x : x[0]) # 개선1
roomArr = []    # 개선2 (최소힙)

for i in range(N) :
    if len(roomArr) == 0 or roomArr[0] > arr[i][0] :    # 종료시간이 가장 빠른 room보다 시작시간이 빠르면 room 추가
        heapq.heappush(roomArr, arr[i][1])
    else :
        heapq.heappop(roomArr)  # 강의 추가 후에는 가장 작은값이 0인덱스로 오도록 (heap 사용시 O(logN))
        heapq.heappush(roomArr, arr[i][1])  # O(log(len(roomArr)))

print(len(roomArr))


# 코드1 : 시간초과 / arr 정렬 안함 => 최적의 room을 찾아다녀야함 (*len(roomArr))
'''
roomArr = []    # 끝나는 시간 기록, 오름차순 정렬

for i in range(N) :  # O(N*len(roomArr))
    ilc = 0
    for j in range(len(roomArr)) :  # O(len(roomArr)) / arr 정렬하면 불필요한 for문
        if arr[i][0] >= roomArr[j] :
            roomArr[j] = arr[i][1]
            ilc = 1

    if ilc == 0 :
        roomArr.append(arr[i][1])
    
    roomArr.sort(reverse = True)  # O(len(roomArr))

print(len(roomArr))
'''

# 코드2 : 시간초과 / 수업 추가마다 roomArr을 재정렬 (O(N*len(roomArr)))
'''
arr.sort(key = lambda x : x[0]) # 개선1
roomArr = []    # 끝나는 시간 기록, 오름차순 정렬

for i in range(N) :  # O(N*len(roomArr))
    if len(roomArr) == 0 or roomArr[0] > arr[i][0] :
        roomArr.insert(0, arr[i][1])
    else :
        roomArr[0] = arr[i][1]

    # roomArr 재정렬 (오름차순)
    for j in range(1, len(roomArr)) :  # O(len(roomArr))
        if roomArr[0] > roomArr[j] :
            roomArr[0], roomArr[j] = roomArr[j], roomArr[0]

print(len(roomArr))
'''
