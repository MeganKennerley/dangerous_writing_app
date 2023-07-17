from tkinter import *

timer = None


def inactive():
    text_box.destroy()
    new_text_box = Text(width=45, height=30)
    new_text_box.focus()
    new_text_box.grid(column=1, row=2)


def reset_timer(event=None):
    global timer
    if timer is not None:
        root.after_cancel(timer)

    timer = root.after(5000, inactive)


root = Tk()

root.bind_all('<space>', reset_timer)
root.bind_all('<a>', reset_timer)
root.bind_all('<e>', reset_timer)
root.bind_all('<i>', reset_timer)
root.bind_all('<o>', reset_timer)
root.bind_all('<u>', reset_timer)

root.title("Dangerous Writing App")
root.configure(background="beige", padx=50, pady=50)
root.geometry("500x600")

label = Label(text="Start Typing...")
label.configure(bg="beige", pady=10, padx=10)
label.grid(column=1, row=1)

label2 = Label(text="Your writing will delete if you stop for longer than 5 seconds!")
label2.configure(bg="beige", fg="red", pady=10, padx=10)
label2.grid(column=1, row=0)

text_box = Text(width=45, height=30)
text_box.focus()
text_box.grid(column=1, row=2)

reset_timer()
root.mainloop()
