# 이번 해가 몇 % 지났는지 출력하는 프로그램 작성

# 입력
# 첫째 줄에, Month DD, YYYY HH:MM과 같이 주어짇나. Month는 현재 월이고, YYYY는 현재 연도이다.
# 숫자 네라지이다. DD, HH, MM은 모두 2자리 숫자이고, 현재 일, 시, 분이다.
# Month는 January, February, March, April, May, June, July,
# August, September, October, November, December 중의 하나이고,
# 연도는 1800보다 크거나 같고, 2600보다 작거나 같다.
# 항상 올바른 날짜와 시간만 입력으로 주어진다.


import sys
from datetime import datetime
input = sys.stdin.readline

today = input().rstrip()
today = datetime.strptime(today, "%B %d, %Y %H:%M")
start_year = datetime(today.year, 1, 1, 0, 0, 0)
next_year = datetime(today.year + 1, 1, 1, 0, 0, 0)

today_seconds = (today - start_year).total_seconds()
next_year_seconds = (next_year - start_year).total_seconds()

print((today_seconds / next_year_seconds) * 100)
