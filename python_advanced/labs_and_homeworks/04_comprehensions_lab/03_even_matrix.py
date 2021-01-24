print([[int(num) for num in input().split(", ") if int(num) % 2 == 0]for row in range(int(input()))])
