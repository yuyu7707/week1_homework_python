name = input("氏名:")
birthday = input("西暦/月/日:")

year, month, day = birthday.split("/")
count = 0
for char in name:
    if char.isalnum():
        count += 1

total = count + int(year) + int(month) + int(day)

if total % 6 == 0:
    fortune = "大吉"

elif total % 3 == 0:
    fortune = "中吉"

elif total % 2 == 0:
    fortune = "吉"

else:
    fortune = "凶"

print(f"{name}さんの運勢: {fortune}")
