import sys

input = sys.stdin.readline

N, M = map(int, input().split())
videos = list(map(int, input().split()))

#  범위 설정
left, right = max(videos), sum(videos)
result = right

while left <= right:
    mid = (left + right) // 2
    count, temp_sum = 1, 0

    for video in videos:
        if temp_sum + video > mid:
            count += 1
            temp_sum = video
        else:
            temp_sum += video

    if count <= M:
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)
