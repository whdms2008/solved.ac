import sys


def input():
    return sys.stdin.readline.rstrip()

# 헌내기는 친구가 필요해
# 입력
# 첫째 줄 : 캠퍼스의 크기를 나타내는 N, M
# N,M(1 <= N <= 600)
# 둘째 줄 : N개의 줄에 캠퍼스의 정보
# O : 빈공간, X : 벽, I : 도연이, P : 사람
# 도연이를 기준으로 만날 수 있는 사람의 수를 반환
# 없다면 TT 반환

# ex )
# 3 5
# OOOPO
# OIOOX
# OOOXP
# => 1

# ex2 )
# 3 3
# IOX
# OXP
# XPP
# => TT

N, M = map(int, input().split())

# 