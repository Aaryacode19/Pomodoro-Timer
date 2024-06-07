from tkinter import *  # Import everything from the Tkinter library for creating the GUI
import math  # Import the math library for mathematical operations

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"  # A color code for pink
RED = "#e7305b"  # A color code for red
GREEN = "#9bdeac"  # A color code for green
YELLOW = "#f7f5dd"  # A color code for yellow
FONT_NAME = "Courier"  # The font name to be used in the application
WORK_MIN = 1  # Work session duration in minutes (set to 1 minute for testing)
SHORT_BREAK_MIN = 5  # Duration of a short break in minutes
LONG_BREAK_MIN = 20  # Duration of a long break in minutes
reps = 0  # A counter for repetitions of work/break sessions
timer = None  # A variable to store the timer

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer  # Use the global keyword to access the timer variable
    if timer is not None:  # If the timer is running
        window.after_cancel(timer)  # Cancel the timer
        timer = None  # Reset the timer variable
    canvas_timer_text.itemconfig(timer_text, text="00:00")  # Reset the timer display to "00:00"
    timer_label.config(text="Timer")  # Reset the timer label text to "Timer"
    checkmark.config(text="")  # Clear the checkmarks
    global reps  # Use the global keyword to access the reps variable
    reps = 0  # Reset the repetitions counter

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps  # Use the global keyword to access the reps variable
    reps += 1  # Increment the repetitions counter
    work_sec = WORK_MIN * 60  # Convert work duration from minutes to seconds
    short_break_sec = SHORT_BREAK_MIN * 60  # Convert short break duration from minutes to seconds
    long_break_sec = LONG_BREAK_MIN * 60  # Convert long break duration from minutes to seconds

    if reps % 8 == 0:  # Every 8th repetition is a long break
        count_down(long_break_sec)  # Start counting down the long break
        timer_label.config(text="Break", fg=RED)  # Update the label to show "Break" in red color
    elif reps % 2 == 0:  # Every even repetition (except the 8th) is a short break
        count_down(short_break_sec)  # Start counting down the short break
        timer_label.config(text="Break", fg=PINK)  # Update the label to show "Break" in pink color
    else:  # Odd repetitions are work periods
        count_down(work_sec)  # Start counting down the work session
        timer_label.config(text="Work", fg=GREEN)  # Update the label to show "Work" in green color

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer  # Use the global keyword to access the timer variable
    count_min = math.floor(count / 60)  # Calculate the number of minutes left
    count_sec = count % 60  # Calculate the number of seconds left
    if count_sec < 10:  # If seconds are less than 10, add a leading zero
        count_sec = f"0{count_sec}"
    canvas_timer_text.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # Update the timer text on the canvas
    if count > 0:  # If there is time left
        timer = window.after(1000, count_down, count - 1)  # Call count_down again after 1 second with decremented count
    else:  # If the countdown is finished
        start_timer()  # Start the next timer (work/break)
        marks = ""  # Initialize a string for checkmarks
        work_sessions = math.floor(reps / 2)  # Calculate the number of completed work sessions
        for _ in range(work_sessions):  # Add a checkmark for each completed work session
            marks += "✔"
        checkmark.config(text=marks)  # Update the checkmarks label

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()  # Create the main window
window.title("Pomodoro")  # Set the title of the window
window.config(padx=100, pady=50, bg=YELLOW)  # Configure the window with padding and background color

# Create a canvas to display an image and text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # Create a canvas widget
dragon_img = PhotoImage(file="evolved-neutral-dragon.gif")  # Load an image
canvas.create_image(100, 112, image=dragon_img)  # Place the image on the canvas
canvas.grid(row=2, column=2)  # Place the canvas in the grid

# Create a separate canvas for the timer text
canvas_timer_text = Canvas(width=200, height=50, bg=YELLOW, highlightthickness=0)  # Create another canvas widget for the timer text
timer_text = canvas_timer_text.create_text(100, 25, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))  # Add text to the canvas
canvas_timer_text.grid(row=3, column=2)  # Place the timer text canvas in the grid

# Create a label to display the timer text
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)  # Create a label widget
timer_label.grid(row=1, column=2)  # Place the label in the grid

# Create start and reset buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)  # Create a start button
start_button.grid(row=4, column=1)  # Place the start button in the grid
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)  # Create a reset button
reset_button.grid(row=4, column=3)  # Place the reset button in the grid

# Create a label for checkmarks
checkmark = Label(text="", fg=GREEN, bg=YELLOW)  # Create a label for checkmarks
checkmark.grid(row=5, column=2)  # Place the checkmark label in the grid

window.mainloop()  # Start the main loop of the application
