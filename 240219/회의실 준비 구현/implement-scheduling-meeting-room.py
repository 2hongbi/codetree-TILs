n = int(input())
meetings = [
    list(map(int, input().split()))
    for _ in range(n)
]

sorted_meetings = sorted(meetings, key=lambda x: x[1]) # 회의 끝나는 시간 기준으로 정렬

cnt = 1

# 첫 회의는 무조건 진행
end_time = sorted_meetings[0][1]

for i in range(1, len(sorted_meetings)):
    # 다음 회의의 시작 시간이 현재 회의 끝나는 시간보다 크거나 같다면
    if sorted_meetings[i][0] >= end_time:
        cnt += 1
        end_time = sorted_meetings[i][1]

print(cnt)