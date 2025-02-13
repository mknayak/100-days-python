from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 0.25
LONG_BREAK_MIN = 0.5
reps=0
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps=0
    check_label["text"]="✔"
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text=f"Timer", fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1
    work_sec= int(WORK_MIN*60)
    short_break_sec= int(SHORT_BREAK_MIN*60)
    long_break_sec= int(LONG_BREAK_MIN*60)
    if reps%2 ==1:
        timer_label.config(text=f"Work", fg=GREEN)
        count_down(work_sec)
    elif reps%8==0:
        timer_label.config(text=f"Break", fg=RED)
        count_down(long_break_sec)
    else:
        timer_label.config(text=f"Break", fg=PINK)
        count_down(short_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    if reps > 0:
        count_min=int(count/60)
        count_sec=count%60
        canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
        if count>0:
            window.after(1000, count_down,count -1)
        else:
            if reps%2==0:
                check_label["text"] = check_label["text"]+" ✔"
            start_timer()
    else:
        start_timer()




# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=220, height=224,bg=YELLOW,highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(110, 112, image=img)
timer_text= canvas.create_text(110,125,text="00:00",fill="white", font=("Courier", 36, "bold"))
timer_label= Label(text="Timer", font=("Ariel", 48, "normal"),fg=GREEN,bg=YELLOW)
check_label= Label(text="✔",fg=GREEN,bg=YELLOW)
start_btn=Button(text="Start",command=start_timer,bg=YELLOW)
reset_btn=Button(text="Reset",command=reset_timer,bg=YELLOW)


canvas.grid(column=1, row=1)
timer_label.grid(column=1, row=0)
check_label.grid(column=1, row=3)
start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)


window.mainloop()