import datetime

day1 = datetime.date.today()

deadline_str = input("데드라인 날짜를 입력해주세요.")
year = int(deadline_str[:4])
month = int(deadline_str[4:6])
day = int(deadline_str[6:])

day2 = datetime.date(year, month, day)
diff = day2 - day1

print(f"남은 기한은 {diff.days}일 남았습니다.")

