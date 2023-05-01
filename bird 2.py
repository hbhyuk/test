import random
time = random.randint(1, 24)
weather = random.choice(["화창","흐림"])
print(f"지금 시각은 {time}시입니다.")
if weather == "화창" :
    print("현재 날씨가 화창합니다.")
else :
    print("현재 날씨가 흐리네요.")
if 6 <= time <= 9 or 14 <= time <= 16 :
    print("종달새가 노래를 합니다.")
else :
    print("종달새가 노래를 하지 않습니다.")