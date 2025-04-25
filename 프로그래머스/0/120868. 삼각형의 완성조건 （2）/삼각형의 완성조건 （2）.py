def solution(sides):
    return 2 * min(sides) -1

print(solution(sides=[1, 2]))
"""
i) c > b 인 경우 (새로운 변이 가장 긴 경우)
c > b > a , c < a + b => a < b < c < a + b 이므로
이 경우 c가 될 수 있는 정수의 개수는 (a + b) - b - 1 = a - 1 로
a - 1 개이다.

ii) c < b 인 경우 (기존의 두 변 중 하나가 가장 긴 경우)
c < b, a < b, b < a + c => c < b < a + c 이므로
이 경우 c가 될 수 있는 정수의 개수는 (a + c) - c - 1 = a - 1 로
a - 1 개이다.

iii) c = b 인 경우
이 경우 c가 될 수 있는 정수의 개수는 1개이다.

따라서, c가 될 수 있는 정수의 총 개수는
(a - 1) + (a - 1) + 1 = 2a - 1 개이다.
"""