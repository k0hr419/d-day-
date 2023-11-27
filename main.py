import tkinter as tk
import time

class AddDate:
    def __init__(self):
        self.add_day = tk.Toplevel(window)
        self.add_day.title("정보 입력")
        
        tk.Label(self.add_day, text="날짜 입력").grid(row=0, column=0, sticky=tk.W)
        tk.Label(self.add_day, text="날짜 이름").grid(row=2, column=0, sticky=tk.W)
        self.input_date = tk.Entry(self.add_day)
        self.input_date.grid(row=1, column=0)
        self.input_info = tk.Entry(self.add_day)
        self.input_info.grid(row=3, column=0)
        
        tk.Button(self.add_day, text="확인", command=self.make_date).grid(row=4, column=0, sticky=tk.N)
    
    def make_date(self):
        if self.input_date.get() and self.input_info.get():
            date_list.append(Widget(self.input_date.get(), self.input_info.get()))
            self.add_day.destroy()

def update_date():
    now_time = time.strftime("%Y년 %m월 %d일 (%a)\n%p %I:%M")
    time_now.config(text=now_time)
    time_now.after(1000, update_date)

class Widget:
    def __init__(self, day, name):
        self.division = tk.LabelFrame(widget_area)
        self.division.pack()

        tk.Label(self.division, text=day).pack()
        tk.Label(self.division, text=name).pack()

font_family = {"title": "AppleSDGothicNeoH00", "sub": "AppleSDGothicNeoB00"}
date_list = []

window = tk.Tk()
window.title("D-Day 계산기")
window.config(bg="white")

time_now = tk.Label(window, text=time.strftime("%Y년 %m월 %d일 (%a)\n%p %I:%M"), font=(font_family["title"], 20), bg="white")
time_now.pack()

tk.Button(window, text="새로운 날짜 추가하기", width=60, bg="white", font=(font_family["sub"], 15), command=lambda:AddDate()).pack()
widget_area = tk.LabelFrame(window, bg="white", width=600, height=300)
widget_area.pack()
tk.Label(window, text="Made by Harang Kim / 419khr@gmail.com", bg="white").pack()

update_date()

window.mainloop()
