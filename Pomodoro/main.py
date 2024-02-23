from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
BLUE = "#8acdd7"
PURPLE = "#ac87c5"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(time_text, text="00:00")
    click_label.config(text=" ")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_time():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK", fg=BLUE)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="BREAK", fg=PURPLE)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    # dynamic typing
    if count_sec == 0:
        count_sec = "00"
    elif count_sec <= 9:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_time()
        click = " "
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            click += "✔"
        click_label.config(text=click)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


button_start = Button(text="Start", fg="black", bg="white", command=start_time)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", fg="black", bg="white", command=reset_timer)
button_reset.grid(column=2, row=2)


click_label = Label(text=" ", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
click_label.grid(column=1, row=3)

timer_label = Label(text="TIMER", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

window.mainloop()
