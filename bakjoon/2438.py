from sys import stdin
stdin = open("bakjoon/input.txt", "r") # 테스트 파일을 읽을 때 사용합니다.


lines = []

# 세 줄을 읽습니다. (이전에 읽은 줄의 다음 줄부터 읽습니다)
for _ in range(1):
	lines.append(stdin.readline().rstrip())
count = int(lines[0])
for nbr in range(1,count + 1):
 print('*' * nbr)