'''
https://www.acmicpc.net/problem/10844

<문제>
45656이란 수를 보자.
이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.
N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

< 해설 >
각 숫자가 마지막에 오는 경우를 배열로 저장하여 계산 (cntArr)

끝이 0인 경우는 이전에 1인 경우 / 끝이 9인 경우는 이전에 8인 경우
나머지 숫자들은 x-1, x+1인 경우에 가능

=============================================================

새로운 배열에 기존 배열을 insert하는 방식으로는 복사 안되는 것으로 보여 함수를 만듬
 ex) tmpArr = arr (arr == [1,2,3,4,5])
arr 요소의 값 수정 시 tmpArr 요소의 값도 수정
아무래도 C처럼 arr의 포인터(주소)를 넣는 개념인 듯함
풀고나서 알게 되었지만 copy()라는 함수가 있넹 ㅋ

'''

def copyElement(arr) :  # 배열 복사하기 (copy())
    newArr = []
    for x in arr : 
        newArr.append(x)
    return newArr
cntArr = [0,1,1,1,1,1,1,1,1,1]  # arr[i] = 마지막 숫자가 i인 계단 수의 개수

N = int(input())  # 입력

arrCnt = [0,1,1,1,1,1,1,1,1,1]

for _ in range(N-1) :
    tmpArr = copyElement(arrCnt)
    for i in range(10) :
        if i == 0 :
            cntArr[i] = tmpArr[1]
        elif i == 9 :
            cntArr[i] = tmpArr[8]
        else :
            cntArr[i] = tmpArr[i-1] + tmpArr[i+1]

print(sum(arrCnt) % 1000000000)
