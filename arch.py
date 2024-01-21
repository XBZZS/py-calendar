import calendar
import random

# 获取用户输入的年份和月份
year = int(input("Please enter a year: "))
month = int(input("Please enter a month: "))

# 生成日历表
cal = calendar.monthcalendar(year, month)

# 打印月份和年份
month_name = calendar.month_name[month]
year_str = str(year)
title = f"{month_name} {year_str.center(28)}"
print(title)
print(" Sun Mon Tue Wed Thu Fri Sat")  # 修改这一行

# 打印月份的第一周
week_one = cal[0]
for i, day in enumerate(week_one):
    if day == 0:
        print("    ", end="")
    else:
        print(f"{day:3}", end=" ")
print()

# 打印月份的其余周
for week in cal[1:]:
    for day in week:
        if day == 0:
            print("    ", end="")
        else:
            print(f"{day:3}", end=" ")
    print()

# 从外部文件读取颜文字列表
with open("kaomojis.txt", "r") as file:
    kaomojis = file.read().splitlines()

# 随机选择一个颜文字并打印
kaomoji = random.choice(kaomojis)
print(f"\n{kaomoji}  Happy coding! \U0001F680")

# 从外部文件读取名言列表
with open("quotes.txt", "r") as file:
    quotes = file.read().splitlines()

# 随机选择一句名言并打印
quote = random.choice(quotes)
print(f"\n{quote}")