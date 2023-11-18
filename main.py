import tkinter as tk
import time

def new_d_day():
    d_day_info = tk.Toplevel(window)
    d_day_info.title("정보 입력")
    tk.Label(d_day_info, text="현재 날짜")

def update_date():
    now_time = time.strftime("%Y년 %m월 %d일 (%a)\n%p %I:%M")
    time_now.config(text=now_time)
    time_now.after(1000, update_date)

class d_day_widget:
    def __init__(self, day, name):
        self.division = tk.LabelFrame(window)

font_family = {"title": "AppleSDGothicNeoH00", "sub": "AppleSDGothicNeoB00"}

window = tk.Tk()
window.title("D-Day 계산기")
window.config(bg="white")

time_now = tk.Label(window, text=time.strftime("%Y년 %m월 %d일 (%a)\n%p %I:%M"), font=(font_family["title"], 20), bg="white")
time_now.pack()

tk.Button(window, text="새로운 날짜 추가하기", width=60, bg="white", font=(font_family["sub"], 15)).pack()
widget_area = tk.LabelFrame(window).pack()
tk.Label(window, text="Made by Harang Kim / 419khr@gmail.com", bg="white").pack()

update_date()

window.mainloop()