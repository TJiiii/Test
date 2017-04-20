import sys
sys.path.append("./brickbreak")

print("실행하고자 하는 게임을 고르세요:")
print("1. brickbreak")
print("2. turtle_game")
print("[1/2]: ", end="")
a = input()
if a=="1":
    import brickbreak
elif a=="2":
    import turtle_game
else:
    print("모르는 옵션: " + a)
