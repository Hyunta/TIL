import sys
input = sys.stdin.readline

sugar = int(input())
bag = 0
while sugar > 0:
    if sugar % 5 == 0:
        bag += sugar //5
        break
    sugar -= 3
    bag += 1
if sugar < 0:
    print(-1)
else:
    print(bag)

