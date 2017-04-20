import sys
sys.path.append("./brickbreak")

print("실행하고자 하는 게임을 고르세요:")
print("1. brickbreak")
print("2. turtle_game")
print("3. pingpong")
print("[1/2/3]: ", end="")
a = input()
if a=="1":
    import brickbreak
elif a == "2":
    import turtle_game
elif a == "3":
    import pingpong
else:
    print("모르는 옵션: " + a)
