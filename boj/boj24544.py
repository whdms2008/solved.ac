# 입력
# 첫 번째 줄에 콘텐츠의 개수 N이 주어짐 ( 1 <= N <= 1_000)

# 두번째 줄에 콘텐츠의 흥미도를 나타내는 N개의 정수가 공백을 사이에 두고 주어짐
# i번째로 주어지는 값 A_i는 i번 콘텐츠의 흥미도이다. ( 0 <= A_i <= 1_000_000 )

# 세 번째 줄에는 My뷰에 등록되어 있는지 여부를 나타내느 ㄴn개의 값이 공백을 사이에 두고 주어진다.
# i 번째로 주어지는 값, B_i는 i번 콘텐츠가 이미 My뷰에 등록이 되어있는 경우에는 1, 등록되어있지 않은 경우 에는 0

# 출력
# 첫째줄 전체 콘텐츠의 흥미도의 합출력
# 둘째줄 My뷰에 등록되어있지 않은흥미도의 합을 출력

N = int(input())
con_inter = list(map(int, input().split(" ")))
register_myview_list = map(int, input().split(" "))
answer = 0
for idx, is_register in enumerate(register_myview_list):
    if not is_register:
        answer += con_inter[idx]
print(sum(con_inter))
print(answer)
