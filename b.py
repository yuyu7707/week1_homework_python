name = input("氏名")
berth = input("西暦/月/日")

year, month, day = berth.split("/")  
count = 0
for moji in name:
    if moji.isalnum():
        count += 1

total = count + int(year) + int(month) + int(day)

if total % 6 == 0:
    unsei = "大吉"

elif total % 3 == 0:
    unsei = "中吉"   

elif total  % 2 == 0:
    unsei = "吉"    

else:
    unsei = "凶"

print(name + "さんの運勢：" + unsei)
