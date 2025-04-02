from datetime import datetime

t_year, t_month, t_day = map(int, input().split(" "))
today = datetime(t_year, t_month, t_day)

e_year, e_month, e_day = map(int, input().split(" "))
end_day = datetime(e_year, e_month, e_day)



if datetime(t_year + 1000 if t_year + 1000 <= 9999 else 9999, t_month, t_day) <= end_day:
    print("gg")
else:
    print(f"D-{(end_day - today).days}")