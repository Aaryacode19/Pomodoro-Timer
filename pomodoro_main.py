from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1  # Set the work duration to 1 minute for testing
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    canvas_timer_text.itemconfig(timer_text, text="00:00")  # Corrected line to update canvas_timer_text
    timer_label.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas_timer_text.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# creating a screen or window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# displaying an image on window or screen using canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
dragon_img = PhotoImage(file="evolved-neutral-dragon.gif")
canvas.create_image(100, 112, image=dragon_img)
canvas.grid(row=2, column=2)

# Create a separate canvas for the timer text
canvas_timer_text = Canvas(width=200, height=50, bg=YELLOW, highlightthickness=0)
timer_text = canvas_timer_text.create_text(100, 25, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas_timer_text.grid(row=3, column=2)

# timer text
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=1, column=2)

# start and reset buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=4, column=1)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=4, column=3)

# checkmark
checkmark = Label(text="", fg=GREEN, bg=YELLOW)
checkmark.grid(row=5, column=2)

window.mainloop()
